from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

today = KeyboardButton('/today')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(today)
