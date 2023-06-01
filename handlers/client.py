from aiogram import Dispatcher, types

from keyboards import (inline_buttons, inline_buttons_to, inline_buttons_y,
                       kb_client)


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
