import os


class Config:
    """Configuration settings for the bot."""

    GRADIO_SERVER_NAME = os.getenv("GRADIO_SERVER_NAME", "0.0.0.0")
    GRADIO_PORT = int(os.getenv("GRADIO_PORT", "7860"))

    SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN", "")
    SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET", "")
    SLACK_PORT = int(os.getenv("SLACK_PORT", "3000"))

    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

    APP_NAME = os.getenv("APP_NAME", "multi-bot-pipeline")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    HOST = os.getenv("HOST", "0.0.0.0")