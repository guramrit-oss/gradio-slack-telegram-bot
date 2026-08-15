import re
import threading

from flask import Flask, Response, jsonify, request
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.signature import SignatureVerifier

from app.bots.base_bot import BaseBot
from app.config import Config


class SlackBot(BaseBot):
    def __init__(self, processor):
        super().__init__(processor)
        self.app = Flask(__name__)
        self.client = WebClient(token=Config.SLACK_BOT_TOKEN) if Config.SLACK_BOT_TOKEN else None
        self.signature_verifier = (
            SignatureVerifier(Config.SLACK_SIGNING_SECRET)
            if Config.SLACK_SIGNING_SECRET
            else None
        )
        self.server = None
        self._thread = None
        self._setup_routes()

    def _setup_routes(self):
        @self.app.route("/slack/health", methods=["GET"])
        def health():
            return jsonify({"status": "ok", "service": "slack-bot"})

        @self.app.route("/slack/events", methods=["POST"])
        def events():
            if not self.signature_verifier:
                return jsonify({"error": "Missing Slack signing secret"}), 401

            raw_body = request.get_data(as_text=True)
            if not self.signature_verifier.is_valid_request(raw_body, request.headers):
                return Response(status=403)

            payload = request.get_json(silent=True) or {}

            if payload.get("type") == "url_verification":
                return jsonify({"challenge": payload.get("challenge", "")})

            if payload.get("type") == "event_callback":
                event = payload.get("event", {})

                if event.get("bot_id"):
                    return Response(status=200)

                if event.get("subtype") in ("bot_message", "message_changed"):
                    return Response(status=200)

                if event.get("type") in ("message", "app_mention"):
                    channel = event.get("channel")
                    text = event.get("text", "")
                    user_text = re.sub(r"<@[^>]+>", "", text).strip()

                    if not user_text:
                        return Response(status=200)

                    reply = self.processor.process_message(user_text, source="slack")

                    if self.client and channel:
                        try:
                            self.client.chat_postMessage(channel=channel, text=reply)
                        except SlackApiError as exc:
                            print(f"Slack API error: {exc.response['error']}")

                    return Response(status=200)

            return Response(status=200)

    def start(self):
        if not self.client or not self.signature_verifier:
            self.running = False
            print("Slack bot not started: missing token or signing secret.")
            return

        try:
            from werkzeug.serving import make_server

            self.server = make_server("0.0.0.0", Config.SLACK_PORT, self.app)
            self.running = True
            self._thread = threading.Thread(target=self.server.serve_forever, daemon=True)
            self._thread.start()
            print(f"Slack bot listening on http://0.0.0.0:{Config.SLACK_PORT}/slack/events")
        except Exception as exc:
            self.running = False
            print(f"Slack bot failed to start: {exc}")

    def stop(self):
        self.running = False
        if self.server:
            try:
                self.server.shutdown()
            except Exception:
                pass
            try:
                self.server.server_close()
            except Exception:
                pass
        self.server = None

    def process_message(self, message):
        return self.processor.process_message(message, source="slack")