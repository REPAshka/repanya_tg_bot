from aiogram import Bot
from aiogram.types import Message
from core.keyboards.reply import get_reply_keyboard


async def get_start(message: Message, bot: Bot):
    await message.answer(f'<s>Привет {message.from_user.first_name}. Рад тебя видеть!</s>', reply_markup=get_reply_keyboard())
    # await message.reply(f'<tg-spoiler>Привет {message.from_user.first_name}. Рад тебя видеть!</tg-spoiler>')


async def get_location(message: Message, bot: Bot):
    await message.answer(f'Ты отправил свою локацию! \r\a'
                        f'{message.location.latitude}\r\n{message.location.longitude}')


async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Отлично. Ты отправил картинку, я сохраню её себе.')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, '/home/repa/my_projects/repanya_tg_bot/files/photo.jpg')


async def get_hello(message: Message, bot: Bot):
    await message.answer(f'И тебе привет!')