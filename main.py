import json
import asyncio
import logging
from core.handlers.basic import get_start, get_photo, get_hello
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from core.config import settings
from aiogram.filters import Command



async def start_bot(bot: Bot):
    for admin_id in settings.bots.admin_ids:
        await bot.send_message(admin_id, text='Бот запущен!')


async def stop_bot(bot: Bot):
    for admin_id in settings.bots.admin_ids:
        await bot.send_message(admin_id, text='Бот остановлен!')

async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                                "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
    
    bot = Bot(token=settings.bots.token, parse_mode='HTML')

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_hello, F.text.lower().startswith('привет'))
    
    dp.message.register(get_start, Command(commands=['start', 'run']))
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())