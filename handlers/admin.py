from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
class FSMAdmin(StatesGroup):
    name = State()
    calories = State()
    ingredients = State()
    recipe = State()

@dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message : types.Message):