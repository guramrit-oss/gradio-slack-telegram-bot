class BotManager:
    def __init__(self, gradio_bot=None, slack_bot=None, telegram_bot=None):
        self.gradio_bot = gradio_bot
        self.slack_bot = slack_bot
        self.telegram_bot = telegram_bot

    def start_bots(self):
        for bot in (self.gradio_bot, self.slack_bot, self.telegram_bot):
            if bot is not None:
                bot.start()
        return self.get_bot_status()

    def stop_bots(self):
        for bot in (self.gradio_bot, self.slack_bot, self.telegram_bot):
            if bot is not None:
                bot.stop()
        return self.get_bot_status()

    def handle_message(self, message, source):
        mapping = {
            "gradio": self.gradio_bot,
            "slack": self.slack_bot,
            "telegram": self.telegram_bot,
        }
        bot = mapping.get(source)
        if bot is None:
            return "Unknown source"
        return bot.process_message(message)

    def get_bot_status(self):
        return {
            "gradio": self.gradio_bot.is_running() if self.gradio_bot else False,
            "slack": self.slack_bot.is_running() if self.slack_bot else False,
            "telegram": self.telegram_bot.is_running() if self.telegram_bot else False,
        }