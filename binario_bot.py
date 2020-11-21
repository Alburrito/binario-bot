from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime
import os, random

from credentials import *

MEMES_PATH = 'memes/'

def bot_start(update,context):
    chat_id = update.effective_chat.id
    message = """Bienvenido al bot de El Binario
    Escribe /help para obtener ayuda"""
    context.bot.send_message(chat_id=chat_id, text=message)

def bot_help(update,context):
    chat_id = update.effective_chat.id
    message = """Bienvenido a la ayuda del bot de El Binario
    Aquí tienes un listado de los comandos que tienes a disposición:
    /start - Da un mensaje de bienvenida   
    /help - Muestra esta ayuda
    /hora - Muestra la hora   
    /meme - Muestra una imagen de un meme
    """
    context.bot.send_message(chat_id=chat_id, text=message)

def bot_hora(update,context):
    chat_id = update.effective_chat.id
    message = "La hora es: "
    hora = datetime.now().strftime("%H:%M:%S")
    message += hora
    context.bot.send_message(chat_id=chat_id, text=message)

def bot_meme(update,context):
    chat_id = update.effective_chat.id
    image_path = MEMES_PATH + random.choice(os.listdir(MEMES_PATH))
    with open(image_path, 'rb') as photo:
        context.bot.sendPhoto(chat_id=chat_id, photo=photo, caption="Aquí tienes un meme")

def bot_echo(update,context):
    chat_id = update.effective_chat.id
    user_message = update.message.text
    message = "De momento no entiendo qué significa: " + user_message
    context.bot.send_message(chat_id = chat_id, text=message)


updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', bot_start)
dispatcher.add_handler(start_handler)
help_handler = CommandHandler('help', bot_help)
dispatcher.add_handler(help_handler)
meme_handler = CommandHandler('meme', bot_meme)
dispatcher.add_handler(meme_handler)
hora_handler = CommandHandler('hora', bot_hora)
dispatcher.add_handler(hora_handler)
echo_handler = MessageHandler(Filters.text, bot_echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()