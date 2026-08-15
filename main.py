import time

from app.bots.bot_manager import BotManager
from app.bots.gradio_bot import GradioBot
from app.bots.slack_bot import SlackBot
from app.bots.telegram_bot import TelegramBot
from app.pipeline import PipelineProcessor


def main():
    processor = PipelineProcessor()

    manager = BotManager(
        gradio_bot=GradioBot(processor),
        slack_bot=SlackBot(processor),
        telegram_bot=TelegramBot(processor),
    )

    print("Starting bots...")
    manager.start_bots()

    print(manager.get_bot_status())
    print("Gradio UI: http://localhost:7860")
    print("Slack Event API: http://localhost:3000/slack/events")
    print("Press Ctrl+C to stop the app.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping bots...")
        manager.stop_bots()
        print("Stopped.")


if __name__ == "__main__":
    main()