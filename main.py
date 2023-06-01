import datetime

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

from create_bot import dp
from handlers import admin, client

from sq_database import extract_data_from_table, read_base, sqlite3

# from parser_fit import get_data, get_reciept, get_ingredients


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)

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


storage = MemoryStorage()


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


if week_number % 2 == 0:
    hello_message = 'Неделя чётная'
    for day, recipe_name in RECIPES.items():
        if day == today:
            message_recipe = ', '.join(recipe_name)
            message_breakfast = read_base(recipe_name.pop(0))
            message_supper = read_base(recipe_name.pop())
            # message_dinner = read_base(recipe_name.pop(1))
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


async def on_startup(_):
    print('Bot is online')


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
