from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.utils.callback_data import MacInfo


# select_macbook = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(
#             text='Macbook air 13 M1 2020',
#             callback_data='apple_air_13_m1_2020'
#         )
#     ],[
#         InlineKeyboardButton(
#             text='Macbook air 14 M1 2021',
#             callback_data='apple_air_14_m1_2021'
#         )
#     ],[
#         InlineKeyboardButton(
#             text='Macbook air 16 M1 2019',
#             callback_data='apple_air_16_m1_2019'
#         )
#     ],[
#         InlineKeyboardButton(
#             text='Link',
#             url='https://www.youtube.com'
#         )
#     ],[
#         InlineKeyboardButton(
#             text='Profile',
#             url='https://t.me/repashka'
#         )
#     ]
# ])


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Macbook air 13 M1 2020', callback_data=MacInfo(model='air', size=13, chip='m1', year=2020))
    keyboard_builder.button(text='Macbook air 14 M1 2021', callback_data=MacInfo(model='air', size=14, chip='m1', year=2021))
    keyboard_builder.button(text='Apple Macbook Pro 16 2019', callback_data=MacInfo(model='pro', size=16, chip='i7', year=2019))
    keyboard_builder.button(text='Link', url='https://www.youtube.com')
    keyboard_builder.button(text='Profile', url='https://t.me/repashka')

    keyboard_builder.adjust(3, 2) # сколько кнопок в каждом ряду
    return keyboard_builder.as_markup()


# select_macbook == get_inline_keyboard(), но по разному закодено