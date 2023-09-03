from typing import Final
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = 'YOUR_BOT_TOKEN'
BOT_USERNAME: Final = '@YOUR_USERNAME'


# ppppineapplebot commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thank you for talking to me! I am a pineapple!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am pineapple bot! Please type something to get started')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is custom command')


# Responses

def handle_response(text: str) -> str:
    processed = text.lower()
    # The processed section of the code make the text lowercase and unsensitive
    if 'hello' in processed:
        return 'Hi there!'

    if 'hi' in processed:
        return 'Hello there!'

    if 'how are you' in processed:
        return 'I am fine, thank you!'

    if 'i love python' in processed:
        return 'do not stop coding!'

    return 'I do not understand what you wrote...'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
    #Commands

if __name__ == '__main__':
    print('Starting bot..')
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

#messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

#errors
    app.add_error_handler(error)

#Polling the bot
    print('Polling..')

    app.run_polling(poll_interval=3)



