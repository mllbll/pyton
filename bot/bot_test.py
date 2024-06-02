import telebot
import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

API_TOKEN = '7035595418:AAFnoccy-HwiQTNgzqW9Fy6oxTa3TCjpYsk'

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть страницу', web_app=WebAppInfo(url= 'https://github.com/mllbll/pyton')))
    await message.answer('Привет', reply_markup=markup)

executor.start_polling(dp)

