from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

today = KeyboardButton('/сегодня')
yesterday = KeyboardButton('/вчера')
tommorow = KeyboardButton('/завтра')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(today).add(yesterday).add(tommorow)

breakfast = InlineKeyboardButton(text='/завтрак', callback_data='breakfast')
dinner = InlineKeyboardButton(text='/обед', callback_data='dinner')
supper = InlineKeyboardButton(text='/ужин', callback_data='supper')

inline_buttons = InlineKeyboardMarkup().add(breakfast).add(dinner).add(supper)