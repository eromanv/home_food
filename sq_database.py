import sqlite3
from parser_fit import get_data, get_ingredients, get_reciept

LINKS_NAMES = []


def sql_start():
    global base, cur
    base = sqlite3.connect('food_from_fitstars.db')
    cur = base.cursor()
    if base:
        print('Connection is ok')
    base.execute(
        'CREATE TABLE IF NOT EXISTS recipes(name TEXT PRIMARY KEY, link TEXT PRIMARY KEY, waytocook TEXT, calories INTEGER, ingredients TEXT)')
    base.commit()





LINKS_NAMES = get_data('https://fitstars.ru/recipes')
my_sl = slice(1, 2)
check = dict(list(LINKS_NAMES.items())[my_sl])п
print(type(check))

ingredients = []
reciepts = []

for link, name in check.items():
    '''
    ЛОгика такая.
    У нас есть словарь с именем и ссылкой, пробегаясь по словарю, мы берем и рецепт и индгредиенты, добавляя в таблицу.
    То есть сначала выполнить цикл фор 
    В котором добавляем значения, и ингредиент и рецепт.

    '''
    cur = base.cursor()
    cur.executemany("INSERT INTO mytable (link, name) VALUES (?, ?)")
    ingredient = get_ingredients(link)
    reciept = get_reciept(link)
    ingredients.append(ingredient)
    reciepts.append(reciept)


print(type(ingredients), type(reciepts))



for data in LINKS_NAMES:
     name = data['name']
     link = data['link']


# sql_start()
async def sql_add_command():
    pass
