from aiogram import types
from .app import dp, bot
from .keyboards import inline_kb
from .states import GameStates
from .data_fetcher import get_random
from aiogram.dispatcher import FSMContext

@dp.message_handler(commands='train_ten', state='*')
async def train_ten(message: types.Message, state: FSMContext):
    await GameStates.random_ten.set()
    res = await get_random()
    async with state.proxy() as data:
        data['step'] = 1
        data['answer'] = res.get('gender')
        data['word'] = res.get('word')
    await message.reply(f"{data['step']} из 10. Слово {data['word']}", reply_markup=inline_kb)

@dp.callback_query_handler(lambda c: c.data in ['der','die','das'], state= GameStates.random_ten)
async def button_click_call_back(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    answer = callback_query.data
    async with state.proxy() as data:
        if answer == data['answer']:
            res = await get_random()
            data['step'] += 1
            data['answer'] = res.get('gender')
            data['word'] = res.get('word')
            if data['step'] > 10:
                await bot.send_message(callback_query.from_user.id, 'Игра закончена!')
                await GameStates.start.set()
            else:
                await bot.send_message(callback_query.from_user.id, 'Ты прав!\n' + f"{data['step']} из 10. Слово {data['word']}", reply_markup=inline_kb)
        else:
            await bot.send_message(callback_query.from_user.id, 'Ты не прав!\n', reply_markup=inline_kb)