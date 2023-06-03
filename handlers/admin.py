from aiogram import types
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup

from create_bot import bot, dp
from sq_database import insert_my_receipt


class FSMAdmin(StatesGroup):
    link = State()
    name = State()
    calories = State()
    ingredients = State()
    recipe = State()

# @dp.message_handler(commands='Загрузить', state=None)


async def cm_start(message: types.Message):
    await FSMAdmin.name.set()
    await message.reply('Напиши ссылку на блюдо')

# @dp.message_handler(content_types=['text'], state=FSMAdmin.name)

async def load_link(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['links'] = message.text
    await FSMAdmin.next()
    await message.reply('Напиши название блюда')

async def load_name(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['names'] = message.text
    await FSMAdmin.next()
    await message.reply('Напиши рецепт приготовления')

async def load_recipes(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['reciept'] = message.text
    await FSMAdmin.next()
    await message.reply('Напиши ингрeдиенты и их количество')

async def load_ingredients(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['ingredients'] = message.text
    await FSMAdmin.next()
    await message.reply('Напиши калории и БЖУ, в формате (напр. К 300 БЖУ16 16 83) )')

# @dp.message_handler(content_types=['text'], state=FSMAdmin.calories)


async def load_calories(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['calories'] = message.text
    await insert_my_receipt(state)
    await state.finish()
# @dp.message_handler(content_types=['text'], state=FSMAdmin.ingredients)




# dp.message_handler(content_types=['text'], state=FSMAdmin.recipe)



def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(load_link, state=FSMAdmin.link)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_recipes, state=FSMAdmin.recipe)
    dp.register_message_handler(load_ingredients, state=FSMAdmin.ingredients)
    dp.register_message_handler(load_calories, state=FSMAdmin.calories)


