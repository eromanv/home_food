import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import datetime
from keyboards import kb_client
from parser_fit import get_data, get_reciept
from dotenv import load_dotenv

load_dotenv()


class CustomException(Exception):
    pass


async def on_startup(_):
    print('Bot is online')

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

today = datetime.datetime.now()
yesterday = (today - datetime.timedelta(days=1)).strftime('%A')
tommorow = (today + datetime.timedelta(days=1)).strftime('%A')
today = today.strftime('%A')


RECIPES = {
    'Monday': ['Запечённые куриные яйца в перцах', 'Ризотто с креветками', 'Салат с курицей в медово-горчичном соусе'],
    'Tuesday': ['Сырники из рикотты', 'Салат с курицей в медово-горчичном соусе', 'Жаркое из говядины'],
    'Wednesday': ['Тостадас с яйцом', 'Жаркое из говядины', 'Салат Цезарь'],
    'Thursday': ['Сэндвич с тунцом и рикоттой', 'Салат Цезарь', 'Фунчоза с индейкой'],
    'Friday': ['Брускетты с лососем и пастой из феты и авокадо', 'Фунчоза с индейкой', 'Салат с киноа, кабачками и кукурузой'],
    'Saturday': ['Пудинг с семенами чиа и яблоками', 'Салат с киноа, кабачками и кукурузой', 'Поке с лососем'],
    'Sunday': ['Овсянка без варки с семенами чиа', 'Поке с лососем', 'Салат с креветками, киноа и нутом'],
}

RECIPES_WITH_LINK = get_data('https://fitstars.ru/recipes')


for day, recipe_name in RECIPES.items():
    if day == today:
        message_recipe = ', '.join(recipe_name)
        breakfast = recipe_name.pop(0)
        dinner = recipe_name.pop(1)
        supper = recipe_name.pop()
        for link, name in RECIPES_WITH_LINK.items():
            if dinner == name:
                message_recipe_steps = '\n'.join(get_reciept(link))

            if supper == name:
                message_recipe_steps = '\n'.join(get_reciept(link))
            if breakfast == name:
                message_recipe_steps = '\n'.join(get_reciept(link))

    if day == yesterday:
        message_recipe_yesterday = ', '.join(
            recipe_name)
        dinner = recipe_name.pop(0)
        supper = recipe_name.pop()
    if day == tommorow:
        message_recipe_tommorow = ', '.join(recipe_name)
        dinner = recipe_name.pop(0)
        supper = recipe_name.pop()


# for link, name in RECIPES_WITH_LINK.items():
#     if dinner == name:
#         print(dinner, link)
#         result = get_reciept(link)
#         print(result)


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Стартуем)', reply_markup=kb_client)
    await message.delete()


@dp.message_handler(commands=['сегодня'])
async def today_recipe(message: types.Message):
    await bot.send_message(message.from_user.id, message_recipe)
    await bot.send_message(message.from_user.id, message_recipe_steps)


@dp.message_handler(commands=['вчера'])
async def yesterday_recipe(message: types.Message):
    await bot.send_message(message.from_user.id, message_recipe_yesterday)


@dp.message_handler(commands=['завтра'])
async def tommorow_recipe(message: types.Message):
    await bot.send_message(message.from_user.id, message_recipe_tommorow)

# @dp.message_handler()
# async def echo_send(message: types.Message):
    # await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
