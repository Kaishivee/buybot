from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Рассчитать каллории'),
            KeyboardButton('Информация о боте')
        ],
        [
            KeyboardButton('Купить')
        ]
    ], resize_keyboard=True
)

buying_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Форм с L-карнитином', callback_data='1'),
            InlineKeyboardButton(text='Момордика Харанция', callback_data='2')
        ],
        [
            InlineKeyboardButton(text='Таблетки Аюрслим Хималая', callback_data='3'),
            InlineKeyboardButton(text='Хром хелат', callback_data='4')
        ]
    ]
)
