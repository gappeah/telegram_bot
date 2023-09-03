Pineapple Bot

This is a simple Telegram bot that I created to greet users, answer questions, and respond to commands.
Prerequisites

    Python 3.8+
    BotFather: https://t.me/botfather

Instructions

    Create a Telegram bot using BotFather.
    Get your bot's token and username.
    Install the dependencies:

pip install python-telegram-bot

    Create a file called pineapple_bot.py and copy the code from this README file.
    Replace the TOKEN and BOT_USERNAME variables with your bot's token and username.
    Run the bot:

python pineapple_bot.py

The bot will now be running and listening for messages.
Commands

The bot supports the following commands:

    /start - Greets the user.
    /help - Shows a list of commands.
    /custom - Responds with a custom message.

The bot also responds to messages that contain the following keywords:

    hello
    hi
    how are you
    i love python

In these cases, the bot will respond with a canned message.
Responses

The bot's responses are all hardcoded in the code. To add new responses, you can edit the handle_response() function.
Errors

If the bot encounters an error, it will print the error message to the console.
