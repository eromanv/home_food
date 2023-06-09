from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

today = KeyboardButton('/сегодня')
yesterday = KeyboardButton('/вчера')
tommorow = KeyboardButton('/завтра')
what_to_buy = KeyboardButton('/продукты')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.insert(today).insert(yesterday).insert(tommorow).add(what_to_buy)

breakfast = InlineKeyboardButton(text='/завтрак', callback_data='breakfast_t')
dinner = InlineKeyboardButton(text='/обед', callback_data='dinner_t')
supper = InlineKeyboardButton(text='/ужин', callback_data='supper_t')

inline_buttons = InlineKeyboardMarkup().insert(breakfast).insert(dinner).insert(supper)

breakfast_y = InlineKeyboardButton(text='/завтрак', callback_data='breakfast_y')
dinner_y = InlineKeyboardButton(text='/обед', callback_data='dinner_y')
supper_y = InlineKeyboardButton(text='/ужин', callback_data='supper_y')

inline_buttons_y = InlineKeyboardMarkup().insert(breakfast_y).insert(dinner_y).insert(supper_y)

breakfast_to = InlineKeyboardButton(text='/завтрак', callback_data='breakfast_to')
dinner_to = InlineKeyboardButton(text='/обед', callback_data='dinner_to')
supper_to = InlineKeyboardButton(text='/ужин', callback_data='supper_to')

inline_buttons_to = InlineKeyboardMarkup().insert(breakfast_to).insert(dinner_to).insert(supper_to)