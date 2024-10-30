import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Assuming `love_calculator` is defined in calc.py and imported correctly.
from calc import love_calculator, name_to_value

# Load environment variables from .env file
load_dotenv()

# Your bot token obtained from BotFather
BOT_TOKEN = os.getenv('BOT_TOKEN')

async def start(update: Update, context):
    """Send a message when the command /start is issued."""
    await update.message.reply_text('Hi!')

async def help_command(update: Update, context):
    """Send a message when the command /help is issued."""
    await update.message.reply_text('0 Help!')

async def echo(update: Update, context):
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

async def calcula_amor(update: Update, context):
    args = context.args
    if len(args) == 2:
        name1, name2 = args[0], args[1]
        compatibility = love_calculator(name1, name2)
        mensagem = f'{name1} com {name2} são {compatibility}% compatíveis!'
        print(mensagem)
        await update.message.reply_text(mensagem)
    else:
        await update.message.reply_text("Por favor, forneça exatamente dois nomes para testar a compatibilidade.")

async def oracle(update: Update, context):
    nome = context.args[0]
    valor = name_to_value(nome)
    if valor % 3 == 0:
        await update.message.reply_text(f"{nome} terá um amor verdadeiro!")
    else :
        await update.message.reply_text(f"{nome} vai ter que se virar! xD")

def main():
    """Start the bot."""
    # Create the Application and pass it your bot's token
    application = Application.builder().token(BOT_TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("calculadora", calcula_amor))
    application.add_handler(CommandHandler("oraculo", oracle))

    # on non-command i.e. message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM, or SIGABRT.
    application.run_polling()

if __name__ == '__main__':
    main()
