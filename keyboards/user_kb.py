from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

today = KeyboardButton('/сегодня')
yesterday = KeyboardButton('/вчера')
tommorow = KeyboardButton('/завтра')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(today).add(yesterday).add(tommorow)
