from typing import Final
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup


TOKEN: Final[str] = '7467645069:AAE5NexNiCIIAxRVZ7xsHhq_JzHFh4jG_Uc'
BOT: Final[Bot] = Bot(TOKEN)


def single_button(text, url):
    button = InlineKeyboardButton(text, url)
    keyboard = InlineKeyboardMarkup([[button]])
    return keyboard
