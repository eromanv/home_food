from aiogram import types
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup

from create_bot import bot, dp


class FSMAdmin(StatesGroup):
    name = State()
    calories = State()
    ingredients = State()
    recipe = State()

# @dp.message_handler(commands='Загрузить', state=None)


async def cm_start(message: types.Message):
    await FSMAdmin.name.set()
    await message.reply('Напиши имя блюда')

# @dp.message_handler(content_types=['text'], state=FSMAdmin.name)


async def load_name(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Введи количество калорий в формате К_БЖУ')

# @dp.message_handler(content_types=['text'], state=FSMAdmin.calories)


async def load_calories(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['calories'] = message.text
    await FSMAdmin.next()
    await message.reply('Напиши ингридиенты и их количество')

# @dp.message_handler(content_types=['text'], state=FSMAdmin.ingredients)


async def load_ingredients(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['ingredients'] = message.text
    await FSMAdmin.next()
    await message.reply('Напиши рецепт приготовления')

# dp.message_handler(content_types=['text'], state=FSMAdmin.recipe)


async def load_recipe(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['recipe'] = message.text
    await state.finish()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_calories, state=FSMAdmin.calories)
    dp.register_message_handler(load_ingredients, state=FSMAdmin.ingredients)
    dp.register_message_handler(load_recipe, state=FSMAdmin.recipe)
