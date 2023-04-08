from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from telegram import Bot
import datetime
from telegram import ReplyKeyboardMarkup
import requests
from bs4 import BeautifulSoup
import lxml
from telegram import ReplyKeyboardMarkup

updater = Updater(token='5826007006:AAH6y2-wWMzvxOu80NUtvEs2JeACvedmqxE')

today = datetime.datetime.now().strftime('%A')


def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Привет, я KittyBot!')


def wake_up(update, context):
    # В ответ на команду /start
    # будет отправлено сообщение 'Спасибо, что включили меня'
    chat = update.effective_chat
    button = ReplyKeyboardMarkup([['Вот какие рецепты есть']])
    context.bot.send_message(chat_id=chat.id,
                             text=f'Спасибо, что включили меня. Today is {today}',
                             reply_markup=button
                             )
    if today == 'Tuesday':
        context.bot.send_message(chat_id=chat.id,
                                 text='Сегодня вот такое меню')
    else:
        context.bot.send_message(chat_id=chat.id,
                                 text=f'Сегодня не готово ничего')


updater.dispatcher.add_handler(CommandHandler('start', wake_up))

updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))
updater.start_polling()
updater.idle()
