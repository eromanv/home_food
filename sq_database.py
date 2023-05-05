import re
import sqlite3

#import pandas as pd
from parser_fit import (get_big_recipe, get_calories, get_data,
                        get_ingredients, get_reciept)

RECIPES = {
    'Monday': ['Запечённые куриные яйца в перцах', 'Ризотто с креветками', 'Кукурузный салат'],
    'Tuesday': ['Сырники из рикотты', 'Кукурузный салат', 'Жаркое из говядины'],
    'Wednesday': ['Тостадас с яйцом', 'Жаркое из говядины', 'Салат Цезарь'],
    'Thursday': ['Сэндвич с тунцом и рикоттой', 'Салат Цезарь', 'Фунчоза с индейкой'],
    'Friday': ['Брускетты с лососем и пастой из феты и авокадо', 'Фунчоза с индейкой', 'Салат с киноа, кабачками и кукурузой'],
    'Saturday': ['Пудинг с семенами чиа и яблоками', 'Салат с киноа, кабачками и кукурузой', 'Поке с лососем'],
    'Sunday': ['Овсянка без варки с семенами чиа', 'Поке с лососем', 'Салат с креветками, киноа и нутом'],
}

RECIPES_2 = {
    'Monday': ['Запечённый батат с яйцом', 'Салат с креветками, киноа и нутом', 'Говядина по тайски с овощами и рисом'],
    'Tuesday': ['Шакшука', 'Говядина по тайски с овощами и рисом', 'Салат Цукини с креветками'],
    'Wednesday': ['Тостадас с яйцом', 'Салат Цукини с креветками', 'Моё Жаркое из говядины'],
    'Thursday': ['Сэндвич с тунцом и рикоттой', 'Моё Жаркое из говядины', 'Греческий салат с нутом'],
    'Friday': ['Брускетты с лососем и пастой из феты и авокадо', 'Греческий салат с нутом', 'Салат с курицей в медово-горчичном соусе'],
    'Saturday': ['Пудинг с семенами чиа и яблоками', 'Салат с курицей в медово-горчичном соусе', 'Салат из кабачков с кукурузой и фасолью'],
    'Sunday': ['Овсянка без варки с семенами чиа', 'Салат из кабачков с кукурузой и фасолью', 'Ризотто с креветками'],
}

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
    definition = cur.execute(
        'SELECT links, names FROM mytable WHERE names = ?', (name, ))
    definition = cur.fetchall()
    # definition = list(definition)
    # definition_out = '\n'.join(definition)
    ingredients_list = cur.execute(
        'SELECT ingredients FROM mytable WHERE names = ?', (name, ))
    ingredients_list = cur.fetchall()
    ingredients_list = ingredients_list[0][0]
    # ingredients_list_split = ingredients_list.split()
    ingredients_ul = re.findall(r'[А-ЯЁ()][а-яё\W\d]*', ingredients_list)
    ingredients_total = '\n'.join(ingredients_ul)
    way_to_cook = cur.execute(
        'SELECT reciept FROM mytable WHERE names = ?', (name, ))
    way_to_cook = cur.fetchall()
    way_to_cook = str(way_to_cook[0][0])
    calories = cur.execute(
        'SELECT calories FROM mytable WHERE names = ?', (name, ))
    calories = cur.fetchall()
    calories_list = str(calories[0][0])
    # way_to_cook_out = way_to_cook.split('/n')
    # print(definition, calories, ingredients_list, way_to_cook)
    # outcome = '{} /n Калорийность: {} /n Ингредиенты: {} /n Что нужно сделать? /n {}'.format(definition, calories, ingredients_list, way_to_cook)
    outcome = f'{definition[0][1]} \n{definition[0][0]} \n\nКалорийность: {calories_list} \n\nИнгредиенты: {ingredients_total} \n \nЧто нужно сделать? \n {way_to_cook}'
    # print(ingredients_list_split)
    # print(ingredients_ul)
    # print(ingredients_total)
    # print(outcome)
    # print(definition[0][1])
    return outcome


def insert_my_receipt():
    base = sqlite3.connect('fitstars_new.db')
    cur = base.cursor()
    links = ['in youtube']
    names = ['Моё Жаркое из говядины']
    ingredients = [
        '500 гр. картошки, 500 гр. мяса, 500 гр. лука, кубик бульона']
    reciept = ["В целом, мясо ужариваем, режем лучок полукольцами, кидаем в ужаренное мясо, отдельно жарим картошечку, потом в общую кастрюлю и заливаем водичкой с бульоном"]
    calories = ['К 525 БЖУ 25 13 26']
    zip_data = list(zip(links, names, ingredients, reciept, calories))
    for d in zip_data:
        cur.execute(
            "INSERT INTO mytable (links, names, ingredients, reciept, calories) VALUES (?, ?, ?, ?, ?)", d)
    base.commit()
    base.close()


def test_keys():
    LINKS = []
    base = sqlite3.connect('fitstars_new.db')
    cur = base.cursor()
    for day, dishes in RECIPES.items():
        for dish in dishes:
            cur.execute('SELECT links FROM mytable WHERE names = ?', (dish, ))
            link_recipe = cur.fetchall()
            link_recipe_lst = link_recipe[0]
            LINKS.append(link_recipe_lst)
    base.commit()
    cur.close()
    base.close()
    print(LINKS)
    return LINKS


def insert_the_number_of_items(LINKS):
    base = sqlite3.connect('fitstars_big_recipe.db')
    cur = base.cursor()
    base.execute(
        'CREATE TABLE IF NOT EXISTS mytable (name TEXT, quantity INTEGER, measure TEXT)')
    for link in LINKS:
        link = link[0]
        items = get_big_recipe(link)
        transposed_list = zip(*items)
        query = "INSERT INTO mytable (name, quantity, measure) VALUES (?, ?, ?)"
        for row in transposed_list:
            values = tuple(row)
            cur.execute(query, values)
    cur.execute("""
    CREATE TABLE summarized_table (
        ingredient TEXT,
        total_quantity REAL
    )
    """)
    base.commit()
    query_sum = '''
    INSERT INTO summarized_table (ingredient, total_quantity)
    SELECT name, SUM(quantity)
    FROM mytable
    GROUP BY name
    '''
    cur.execute(query_sum)
    base.commit()
    cur.close()
    base.close()
    print(transposed_list)
    return transposed_list

def extract_data_from_table():
    base = sqlite3.connect('fitstars_big_recipe.db')
    cur = base.cursor()
    cur.execute('SELECT * from summarized_table')
    data = cur.fetchall()
    all_ingredients = []
    to_buy = []
    for element, quantity in data:
        all_ingredients = f'{element}, {quantity}'
        to_buy.append(all_ingredients)
        to_buy_final = [s.split(',') for s in to_buy]
        final_list = '\n'.join([' '.join(inner_list) for inner_list in to_buy_final])
    # print(final_list)
    return final_list

# def make_excel():
#     conn = sqlite3.connect('fitstars_big_recipe.db')
#     df = pd.read_sql_query("SELECT * FROM summarized_table;", conn)
#     df.to_excel('output.xlsx', index=False)
#     conn.close()

# insert_my_receipt()
# sql_start()

# result = collect_information()#
# create_base(result)
# read_base('Брускетты с лососем и пастой из феты и авокадо')
# #result = collect_information()


# print(base)
# print(type(ingredients), type(reciepts))
# LINKS = test_keys()
# insert_the_number_of_items(LINKS)
# make_excel()
extract_data_from_table()