# from parser_fit import get_data, get_reciept, get_ingredients
import datetime

from aiogram import Dispatcher, types

from create_bot import bot, dp
from keyboards import (inline_buttons, inline_buttons_to, inline_buttons_y,
                       kb_client)
from sq_database import extract_data_from_table, read_base, sqlite3

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


'''
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
'''

today = datetime.datetime.now()
week_number = int(today.strftime('%U'))
yesterday = (today - datetime.timedelta(days=1)).strftime('%A')
tommorow = (today + datetime.timedelta(days=1)).strftime('%A')
today = today.strftime('%A')


if week_number % 2 == 0:
    hello_message = 'Неделя чётная'
    for day, recipe_name in RECIPES.items():
        if day == today:
            message_recipe = ', '.join(recipe_name)
            # message_breakfast = read_base(recipe_name.pop(0))
            message_supper = read_base(recipe_name.pop())
            message_dinner = read_base(recipe_name.pop(1))
        if day == yesterday:
            message_recipe_yesterday = ', '.join(
                recipe_name)
            # message_breakfast_y = read_base(recipe_name.pop(0))
            message_supper_y = read_base(recipe_name.pop())
            message_dinner_y = read_base(recipe_name.pop(1))
        if day == tommorow:
            message_recipe_tommorow = ', '.join(recipe_name)
            # message_breakfast_t = read_base(recipe_name.pop(0))
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
            # message_breakfast_y = read_base(recipe_name.pop(0))
            message_supper_y = read_base(recipe_name.pop())
            message_dinner_y = read_base(recipe_name.pop(1))
        if day == tommorow:
            message_recipe_tommorow = ', '.join(recipe_name)
            message_breakfast_t = read_base(recipe_name.pop(0))
            message_supper_t = read_base(recipe_name.pop())
            message_dinner_t = read_base(recipe_name.pop(1))


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, hello_message, reply_markup=kb_client)
    await message.delete()


# @dp.message_handler(commands=['продукты'])


async def all_menu(message: types.Message):
    await bot.send_message(message.from_user.id, food_menu)


# @dp.message_handler(commands=['сегодня'])


async def today_recipe(message: types.Message):
    await bot.send_message(message.from_user.id, message_recipe)
    await message.answer("Chhose the plate", reply_markup=inline_buttons)


# @dp.callback_query_handler(text='breakfast_t')
async def today_recipe_breakfast(message: types.Message):
    await bot.send_message(message.from_user.id, message_breakfast)


# @dp.callback_query_handler(text='dinner_t')
async def today_recipe_dinner(message: types.Message):
    await bot.send_message(message.from_user.id, message_dinner)


# @dp.callback_query_handler(text='supper_t')
async def today_recipe_supper(message: types.Message):
    await bot.send_message(message.from_user.id, message_supper)


# @dp.message_handler(commands=['вчера'])
async def yesterday_recipe(message: types.Message):
    await bot.send_message(message.from_user.id, message_recipe_yesterday)
    await message.answer("Chose the plate", reply_markup=inline_buttons_y)


# @dp.callback_query_handler(text='breakfast_y')
async def yesterday_recipe_breakfast(message: types.Message):
    await bot.send_message(message.from_user.id, message_breakfast_y)


# @dp.callback_query_handler(text='dinner_y')
async def yesterday_recipe_dinner(message: types.Message):
    await bot.send_message(message.from_user.id, message_dinner_y)


# @dp.callback_query_handler(text='supper_y')
async def yesterday_recipe_supper(message: types.Message):
    await bot.send_message(message.from_user.id, message_supper_y)


# @dp.message_handler(commands=['завтра'])
async def tommorow_recipe(message: types.Message):
    await bot.send_message(message.from_user.id, message_recipe_tommorow)
    await message.answer("Chose the plate", reply_markup=inline_buttons_to)


# @dp.callback_query_handler(text='breakfast_to')
async def tommorow_recipe_breakfast(message: types.Message):
    await bot.send_message(message.from_user.id, message_breakfast_t)


# @dp.callback_query_handler(text='dinner_to')
async def tommorow_recipe_dinner(message: types.Message):
    await bot.send_message(message.from_user.id, message_dinner_t)


# @dp.callback_query_handler(text='supper_to')
async def tommorow_recipe_supper(message: types.Message):
    await bot.send_message(message.from_user.id, message_supper_t)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=["start", "help"])
    dp.register_message_handler(all_menu, commands=["продукты"])
    dp.register_message_handler(today_recipe, commands=["сегодня"])
    dp.register_callback_query_handler(
        today_recipe_breakfast, text="breakfast_t")
    dp.register_callback_query_handler(today_recipe_dinner, text="dinner_t")
    dp.register_callback_query_handler(today_recipe_supper, text="supper_t")
    dp.register_message_handler(yesterday_recipe, commands=["вчера"])
    dp.register_callback_query_handler(
        yesterday_recipe_breakfast, text="breakfast_y")
    dp.register_callback_query_handler(
        yesterday_recipe_dinner, text="breakfast_d")
    dp.register_callback_query_handler(
        yesterday_recipe_supper, text="breakfast_s")
    dp.register_message_handler(tommorow_recipe, commands=["завтра"])
    dp.register_callback_query_handler(
        tommorow_recipe_breakfast, text="breakfast_to")
    dp.register_callback_query_handler(
        tommorow_recipe_dinner, text="dinner_to")
    dp.register_callback_query_handler(
        tommorow_recipe_supper, text="supper_to")
