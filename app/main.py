from app.bots.bot_manager import BotManager
from app.pipelines.router import Router

def main():
    # Initialize the bot manager
    bot_manager = BotManager()

    # Initialize the router for handling incoming messages
    router = Router(bot_manager)

    # Start the bots
    bot_manager.start_bots()

    # Start the message routing
    router.start_routing()

if __name__ == "__main__":
    main()