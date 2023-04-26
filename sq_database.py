import sqlite3
from parser_fit import get_data, get_ingredients, get_reciept, get_calories

LINKS_NAMES = []
LINKS_NAMES = get_data('https://fitstars.ru/recipes')
links = []
names = []
ingredients = []
reciepts = []
calories = []

def sql_start():
    global base, cur
    base = sqlite3.connect('fitstars_new.db')
    cur = base.cursor()
    if base:
        print('Connection is ok')
    base.execute(
        'CREATE TABLE IF NOT EXISTS mytable (links TEXT, names TEXT, reciept TEXT, ingredients TEXT, calories TEXT)')
    base.commit()
    base.close()

# my_sl = slice(1, 3)
# check = dict(list(LINKS_NAMES.items())[my_sl])
# print(type(check))
# print(check)


def collect_information():
    for link, name in LINKS_NAMES:
        '''
        ЛОгика такая.
        У нас есть словарь с именем и ссылкой, пробегаясь по словарю, мы берем и рецепт и индгредиенты, добавляя в таблицу.
        То есть сначала выполнить цикл фор
        В котором добавляем значения, и ингредиент и рецепт.'''

        links.append(link)
        names.append(name)
        # cur.executemany("INSERT INTO mytable (link, name) VALUES (?, ?)", LINKS_NAMES)
        ingredient = get_ingredients(link)
        ingredients.append(ingredient)
        # cur.execute("INSERT INTO mytable (ingredients) VALUES (?)", ingredient)
        reciept = get_reciept(link)
        reciepts.append(reciept)
        # cur.execute("INSERT INTO mytable (reciept) VALUES (?)", (reciept,))
        # ingredients.append(ingredient)
        # reciepts.append(reciept)
        calorie = get_calories(link)
        calories.append(calorie)
        data = list(zip(links, names, ingredients, reciepts, calories))
    return data


def create_base(data):
    sql_start()
    base = sqlite3.connect('fitstars_new.db')
    cur = base.cursor()
    for d in data:
        cur.execute(
            "INSERT INTO mytable (links, names, ingredients, reciept, calories) VALUES (?, ?, ?, ?, ?)", d)
    base.commit()
    base.close()


def read_base(name):
    base = sqlite3.connect('fitstars_new.db')
    if base:
        print('Connection to read - is ok')
    cur = base.cursor()
    definition = cur.execute('SELECT links, names FROM mytable WHERE names = ?', (name, ))
    definition = cur.fetchall()
    # definition = list(definition)
    # definition_out = ', '.join(definition)
    ingredients_list = cur.execute('SELECT ingredients FROM mytable WHERE names = ?', (name, ))
    ingredients_list = cur.fetchall()
    # ingredients_list_out = ingredients_list.split('/n')
    way_to_cook = cur.execute(
        'SELECT reciept FROM mytable WHERE names = ?', (name, ))
    way_to_cook = cur.fetchall()
    calories = cur.execute('SELECT calories FROM mytable WHERE names = ?', (name, ))
    calories = cur.fetchall()
    # way_to_cook_out = way_to_cook.split('/n')
    print(definition, calories, ingredients_list, way_to_cook)
    return definition, calories, ingredients_list, way_to_cook

sql_start()

result = collect_information()
create_base(result)
# read_base('Ризотто с креветками')
# #result = collect_information()


# print(base)
# print(type(ingredients), type(reciepts))
