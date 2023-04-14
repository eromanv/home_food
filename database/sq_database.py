from sqlite3 import sq


def sql_start():
    global base, cur
    base = sq.connect('food_from_fitstars.db')
    cur = base.cursor()
    if base:
        print('Connection is ok')
    base.execute(
        'CREATE TABLE IF NOT EXISTS recipes(name TEXT PRIMARY KEY, link TEXT, waytocook TEXT)')
    base.commit()


async def sql_add_command():
    pass
