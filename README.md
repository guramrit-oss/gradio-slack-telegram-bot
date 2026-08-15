# Multi-Bot Gradio + Slack + Telegram Project

This project runs a shared message pipeline across:
- Gradio web interface
- Slack Event API bot
- Telegram bot

## Setup

1. Create venv
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

## Project Structure

```
gradio-slack-telegram-bot
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   ├── bots
│   │   ├── __init__.py
│   │   ├── gradio_bot.py
│   │   ├── slack_bot.py
│   │   ├── telegram_bot.py
│   │   └── bot_manager.py
│   ├── pipelines
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── router.py
│   │   ├── workflow.py
│   │   └── steps.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── message_service.py
│   │   └── event_bus.py
│   └── utils
│       ├── __init__.py
│       └── logging.py
├── tests
│   ├── __init__.py
│   └── test_pipelines.py
├── .env.example
├── .gitignore
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd gradio-slack-telegram-bot
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables by copying `.env.example` to `.env` and filling in the necessary values.

## Usage

To run the bot, execute the following command:
```
python app/main.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.