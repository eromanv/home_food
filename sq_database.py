import sqlite3
from parser_fit import get_data, get_ingredients, get_reciept

LINKS_NAMES = []
LINKS_NAMES = get_data('https://fitstars.ru/recipes')
links = []
names = []
ingredients = []
reciepts = []


def sql_start():
    global base, cur
    base = sqlite3.connect('fitstars_new.db')
    cur = base.cursor()
    if base:
        print('Connection is ok')
    base.execute(
        'CREATE TABLE IF NOT EXISTS mytable (links TEXT, names TEXT, reciept TEXT, ingredients TEXT)')
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
        В котором добавляем значения, и ингредиент и рецепт.

        '''
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
        data = list(zip(links, names, ingredients, reciepts))
    return data


def create_base(data):
    sql_start()
    base = sqlite3.connect('fitstars_new.db')
    cur = base.cursor()
    for d in data:
        cur.execute(
            "INSERT INTO mytable (links, names, ingredients, reciept) VALUES (?, ?, ?, ?)", d)
    base.commit()
    base.close()


def read_base(link):
    base = sqlite3.connect('fitstars_new.db')
    cur = base.cursor()
    cur.execute('SELECT * FROM mytable WHERE links = ?', (link, ))
    result = cur.fetchall()
    print(result)
    return result


read_base('https://fitstars.ru/recipes/zapechyonnye-kurinye-yajca-v-tortili')
# #result = collect_information()
# create_base(result)

# print(base)
# print(type(ingredients), type(reciepts))


# sql_start()
async def sql_add_command():
    pass
