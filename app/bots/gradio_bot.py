import threading

import gradio as gr

from app.bots.base_bot import BaseBot
from app.config import Config 


class GradioBot(BaseBot):
    def __init__(self, processor):
        super().__init__(processor)
        self.server_name = Config.GRADIO_SERVER_NAME
        self.server_port = Config.GRADIO_PORT
        self.interface = self._build_interface()

    def _build_interface(self):
        def respond(message):
            if not message:
                return "Please enter a message."
            return self.processor.process_message(message, source="gradio")

        return gr.ChatInterface(
            fn=respond,
            title="Gradio Bot",
            description="Shared multi-bot assistant",
        )

    def start(self):
        self.running = True
        thread = threading.Thread(
            target=self.interface.launch,
            kwargs={"server_name": self.server_name, "server_port": self.server_port, "share": False},
            daemon=True,
        )
        thread.start()
        print(f"Gradio bot running on http://localhost:{self.server_port}")

    def stop(self):
        self.running = False
        try:
            self.interface.close()
        except Exception:
            pass

    def process_message(self, message):
        return self.processor.process_message(message, source="gradio")