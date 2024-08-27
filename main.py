from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

import texts
from bot_key import API
from keyboards import *

bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(texts.greet, reply_markup=start_kb)


@dp.message_handler(text='Рассчитать каллории')
async def set_age(message, state):
    await message.answer(texts.age)
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer(texts.growth)
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer(texts.weight)
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    weight_ = data["weight"]
    growth_ = data["growth"]
    age_ = data["age"]
    calories = 10 * int(weight_) + int(6.25) * int(growth_) - 5 * int(age_) - 161
    await message.answer(f'Ваша норма калорий: {calories}', reply_markup=start_kb)
    await state.finish()


@dp.message_handler(text='Информация о боте')
async def help_(message: types.Message):
    await message.answer(texts.info, reply_markup=start_kb)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    with open('product_1.png', 'rb') as img1:
        await message.answer_photo(img1, texts.product1 + '\n' + texts.product1_info + '\n' + texts.price1)

    with open('product_2.png', 'rb') as img2:
        await message.answer_photo(img2, texts.product2 + '\n' + texts.product2_info + '\n' + texts.price2)

    with open('product_3.jpg', 'rb') as img3:
        await message.answer_photo(img3, texts.product3 + '\n' + texts.product3_info + '\n' + texts.price3)

    with open('product_4.png', 'rb') as img4:
        await message.answer_photo(img4, texts.product4 + '\n' + texts.product4_info + '\n' + texts.price4)

    await message.answer('Что хочешь приобрести?', reply_markup=buying_kb)


@dp.callback_query_handler(text='1')
async def buying1(call):
    await call.message.answer(texts.buy, reply_markup=start_kb)
    await call.answer()


@dp.callback_query_handler(text='2')
async def buying2(call):
    await call.message.answer(texts.buy, reply_markup=start_kb)
    await call.answer()


@dp.callback_query_handler(text='3')
async def buying3(call):
    await call.message.answer(texts.buy, reply_markup=start_kb)
    await call.answer()


@dp.callback_query_handler(text='4')
async def buying4(call):
    await call.message.answer(texts.buy, reply_markup=start_kb)
    await call.answer()


@dp.message_handler()
async def help_(message: types.Message):
    await message.answer(texts.start_message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
