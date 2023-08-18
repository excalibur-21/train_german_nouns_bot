from aiogram import types
from .app import dp
from . import messages

@dp.message_handler(commands=('start', 'help'))
async def send_welcome(message: types.Message):
    await message.reply(messages.WELCOME_MESSAGE)