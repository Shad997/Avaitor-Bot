from typing import Final
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup


TOKEN: Final[str] = '7467645069:AAE5NexNiCIIAxRVZ7xsHhq_JzHFh4jG_Uc'
BOT: Final[Bot] = Bot(TOKEN)


def single_button(text, url):
    button = InlineKeyboardButton(text, url)
    keyboard = InlineKeyboardMarkup([[button]])
    return keyboard

async def send_session_start(chat_id):
    await BOT.send_sticker(chat_id, 'static/session_starts.webp')

async def send_session_close(chat_id):
    await BOT.send_sticker(chat_id, 'static/session_closed.webp')


