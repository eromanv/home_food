from aiogram.utils import executor

from create_bot import dp
from handlers import admin, client


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)


async def on_startup(_):
    print('Bot is online')


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
