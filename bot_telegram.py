import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import datetime
from keyboards import kb_client
# from parser_fit import get_data
from dotenv import load_dotenv

load_dotenv()


class CustomException(Exception):
    pass


async def on_startup(_):
    print('Bot is online')

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

today = datetime.datetime.now().strftime('%A')

RECIPES = {
    'Monday': ['Курица терияки с рисом', 'Салат с нутом и тунцом'],
    'Tuesday': ['Говядина по монгольски с рисом', 'Салат с нутом и тунцом'],
    'Wednesday': ['Киноа с авокадо и семечками', 'Греческий салат с нутом'],
    'Thursday': ['Тилапия в кляре', 'Жаркое из говядины'],
    'Friday': ['Жаркое из говядины', 'Салат с креветками, киноа и нутом'],
    'Saturday': ['Ролл с курицей и авокадо', 'Креветки кунг-пао с рисом'],
    'Sunday': ['Креветки кунг-пао с рисом', 'Рис с овощами'],
}

for day, recipe_name in RECIPES.items():
    if day == today:
        message_recipe = ', '.join(recipe_name)
        dinner = recipe_name.pop(0)
        supper = recipe_name.pop()
#        print(dinner)
#        print(supper)

RECIPES_WITH_LINK = get_data('https://fitstars.ru/recipes')


for link, name in RECIPES_WITH_LINK.items():
    if dinner == name:
        print(dinner, link)



@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Стартуем)', reply_markup=kb_client)
    await message.delete()


@dp.message_handler(commands=['today'])
async def today_recipe(message: types.Message):
    await bot.send_message(message.from_user.id, message_recipe)


# @dp.message_handler()
# async def echo_send(message: types.Message):
    # await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
