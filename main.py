import json
import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ContentType
from aiogram.filters import Command
from core.config import settings
from core.filters.is_contact import IsTrueContact
from core.utils.commands import set_commands
from core.utils.callback_data import MacInfo
from core.handlers.basic import get_start, get_photo, get_hello, get_location, get_inline
from core.handlers.contact import get_true_contact, get_fake_contact
from core.handlers.callback import select_macbook



async def start_bot(bot: Bot):
    await set_commands(bot)
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
    dp.message.register(get_inline, Command(commands='inline'))
    dp.callback_query.register(select_macbook, MacInfo.filter())
    dp.message.register(get_location, F.content_type==ContentType.LOCATION)
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_hello, F.text.lower().startswith('привет'))
    dp.message.register(get_true_contact, F.content_type==ContentType.CONTACT, IsTrueContact())
    dp.message.register(get_fake_contact, F.content_type==ContentType.CONTACT)
    dp.message.register(get_start, Command(commands=['start', 'run']))
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())