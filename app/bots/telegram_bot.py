class TelegramBot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = f"https://api.telegram.org/bot{self.api_key}/"

    def send_message(self, chat_id, text):
        url = f"{self.base_url}sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": text
        }
        response = requests.post(url, json=payload)
        return response.json()

    def get_updates(self):
        url = f"{self.base_url}getUpdates"
        response = requests.get(url)
        return response.json()

    def handle_updates(self):
        updates = self.get_updates()
        for update in updates.get("result", []):
            chat_id = update["message"]["chat"]["id"]
            text = update["message"]["text"]
            self.send_message(chat_id, f"You said: {text}")