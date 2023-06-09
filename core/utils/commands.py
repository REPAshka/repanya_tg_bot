from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
        BotCommand(
            command='help',
            description='Помощь'
        ),
        BotCommand(
            command='cancel',
            description='Сбросить'
        ),
        BotCommand(
            command='inline',
            description='Показать инлайн клавиатуру'
        ),
        BotCommand(
            command='pay',
            description='Задонатить на пиво'
        )
    ]
    
    await bot.set_my_commands(commands, BotCommandScopeDefault())
    # https://core.telegram.org/type/BotCommandScope - ссылка на описалово Scope'ов
    # , т.е. видимости комманд для определённых пользователей