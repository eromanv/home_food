import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import datetime
from keyboards import kb_client, inline_buttons, inline_buttons_y, inline_buttons_to
# from parser_fit import get_data, get_reciept, get_ingredients
from dotenv import load_dotenv
from sq_database import read_base, sqlite3, extract_data_from_table

load_dotenv()

RECIPES = {
    'Monday': ['Рисовый пудинг', 'Ризотто с креветками', 'Салат с курицей в медово-горчичном соусе'],
    'Tuesday': ['Шоколадная каша с клубникой', 'Салат с курицей в медово-горчичном соусе', 'Жаркое из говядины'],
    'Wednesday': ['Сэндвич с яичным салатом', 'Жаркое из говядины', 'Тако с креветками'],
    'Thursday': ['Французский тост с клубникой', 'Тако с креветками', 'Поке с лососем'],
    'Friday': ['Жареный картофель с ветчиной', 'Поке с лососем', 'Салат Цезарь'],
    'Saturday': ['Тост с авокадо и лососем', 'Салат Цезарь', 'Сливочно огуречный салат с котлетами из индейки'],
    'Sunday': ['Базовые блинчики', 'Сливочно огуречный салат с котлетами из индейки', 'Салат из кабачков с кукурузой и фасолью'],
}

RECIPES_2 = {
    'Monday': ['Омлет с цукини', 'Салат из кабачков с кукурузой и фасолью', 'Фунчоза с индейкой'],
    'Tuesday': ['Скандинавский сэндвич с яйцом и лососем', 'Фунчоза с индейкой', 'Жаренная говядина с брокколи'],
    'Wednesday': ['Семена чиа с ягодами', 'Жаренная говядина с брокколи', 'Салат Цукини с креветкам'],
    'Thursday': ['Сэндвич с беконом', 'Салат Цукини с креветкам', 'Говядина по тайски с овощами и рисом'],
    'Friday': ['Омлет с сыром фета', 'Говядина по тайски с овощами и рисом', 'Салат с креветками, киноа и нутом'],
    'Saturday': ['Овсянка с арахисовым маслом и джемом', 'Салат с креветками, киноа и нутом', 'Моё жаркое'],
    'Sunday': ['Базовые блинчики', 'Моё жаркое', 'Ризотто с креветками'],
}

# RECIPES_WITH_LINK = get_data('https://fitstars.ru/recipes')
TOKEN = os.getenv('TOKEN')

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)



def test_keys():
    base = sqlite3.connect('fitstars_new.db')
    cur = base.cursor()
    for day, dishes in RECIPES.items():
        name = dishes
    link = cur.execute('SELECT links FROM mytable WHERE name = ?', (name, ))
    
    print(dishes)
    return dishes

class CustomException(Exception):
    pass




today = datetime.datetime.now()
week_number = int(today.strftime('%U'))
yesterday = (today - datetime.timedelta(days=1)).strftime('%A')
tommorow = (today + datetime.timedelta(days=1)).strftime('%A')
today = today.strftime('%A')


# def prepare_message():


#     return message_breakfast, message_dinner, message_supper


if week_number % 2 == 0:
    hello_message = 'Неделя чётная'
    for day, recipe_name in RECIPES.items():
        if day == today:
            message_recipe = ', '.join(recipe_name)
            message_breakfast = read_base(recipe_name.pop(0))
            message_supper = read_base(recipe_name.pop())
            message_dinner = read_base(recipe_name.pop(1))
        if day == yesterday:
            message_recipe_yesterday = ', '.join(
                recipe_name)
            message_breakfast_y = read_base(recipe_name.pop(0))
            message_supper_y = read_base(recipe_name.pop())
            message_dinner_y = read_base(recipe_name.pop(1))
        if day == tommorow:
            message_recipe_tommorow = ', '.join(recipe_name)
            message_breakfast_t = read_base(recipe_name.pop(0))
            message_supper_t = read_base(recipe_name.pop())
            message_dinner_t = read_base(recipe_name.pop(1))
else:
    hello_message = 'Неделя нечетная'
    for day, recipe_name in RECIPES_2.items():
        if day == today:
            message_recipe = ', '.join(recipe_name)
            message_breakfast = read_base(recipe_name.pop(0))
            message_supper = read_base(recipe_name.pop())
            message_dinner = read_base(recipe_name.pop(1))
        if day == yesterday:
            message_recipe_yesterday = ', '.join(
                recipe_name)
            message_breakfast_y = read_base(recipe_name.pop(0))
            message_supper_y = read_base(recipe_name.pop())
            message_dinner_y = read_base(recipe_name.pop(1))
        if day == tommorow:
            message_recipe_tommorow = ', '.join(recipe_name)
            message_breakfast_t = read_base(recipe_name.pop(0))
            message_supper_t = read_base(recipe_name.pop())
            message_dinner_t = read_base(recipe_name.pop(1))
       #
        # breakfast = recipe_name.pop(0)
        # dinner = recipe_name.pop(1)
        # supper = recipe_name.pop()
        


food_menu = extract_data_from_table()
# for link, name in RECIPES_WITH_LINK.items():
#     if dinner == name:
#         print(dinner, link)
#         result = get_reciept(link)
#         print(result)



async def on_startup(_):
    print('Bot is online')


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, hello_message, reply_markup=kb_client)
    await message.delete()

@dp.message_handler(commands=['продукты'])
async def all_menu(message: types.Message):
    await bot.send_message(message.from_user.id, food_menu)

@dp.message_handler(commands=['сегодня'])
async def today_recipe(message: types.Message):
    await bot.send_message(message.from_user.id, message_recipe)
    await message.answer('Chhose the plate', reply_markup=inline_buttons)


@dp.callback_query_handler(text='breakfast_t')
async def today_recipe_breakfast(message: types.Message):
    await bot.send_message(message.from_user.id, message_breakfast)


@dp.callback_query_handler(text='dinner_t')
async def today_recipe_dinner(message: types.Message):
    await bot.send_message(message.from_user.id, message_dinner)


@dp.callback_query_handler(text='supper_t')
async def today_recipe_supper(message: types.Message):
    await bot.send_message(message.from_user.id, message_supper)


@dp.message_handler(commands=['вчера'])
async def yesterday_recipe(message: types.Message):
    await bot.send_message(message.from_user.id, message_recipe_yesterday)
    await message.answer('Chose the plate', reply_markup=inline_buttons_y)


@dp.callback_query_handler(text='breakfast_y')
async def yesterday_recipe_breakfast(message: types.Message):
    await bot.send_message(message.from_user.id, message_breakfast_y)


@dp.callback_query_handler(text='dinner_y')
async def yesterday_recipe_dinner(message: types.Message):
    await bot.send_message(message.from_user.id, message_dinner_y)


@dp.callback_query_handler(text='supper_y')
async def yesterday_recipe_supper(message: types.Message):
    await bot.send_message(message.from_user.id, message_supper_y)


@dp.message_handler(commands=['завтра'])
async def tommorow_recipe(message: types.Message):
    await bot.send_message(message.from_user.id, message_recipe_tommorow)
    await message.answer('Chose the plate', reply_markup=inline_buttons_to)


@dp.callback_query_handler(text='breakfast_to')
async def tommorow_recipe_breakfast(message: types.Message):
    await bot.send_message(message.from_user.id, message_breakfast_t)


@dp.callback_query_handler(text='dinner_to')
async def tommorow_recipe_dinner(message: types.Message):
    await bot.send_message(message.from_user.id, message_dinner_t)


@dp.callback_query_handler(text='supper_to')
async def tommorow_recipe_supper(message: types.Message):
    await bot.send_message(message.from_user.id, message_supper_t)


# @dp.message_handler()
# async def echo_send(message: types.Message):
    # await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
