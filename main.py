import string

import config
import logging

import random

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import executor
from aiogram import types
import json

logging.basicConfig(level=logging.INFO)


bot = Bot(token=config.TOKEN)

dp = Dispatcher(bot)

@dp.message_handler()
async def echo_send(message: types.Message):
    strarr = ["ИПСА не відміняється, еее", "Ты, точно, ИПСАшник?", "Тебя ИПСА склонила?"]
    if{i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}.intersection(set(json.load(open('IASA.json')))) != set():
        await message.reply(random.choice(strarr))

if __name__ == "__main__":

    executor.start_polling(dp, skip_updates=True)