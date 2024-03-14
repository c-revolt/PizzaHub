from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f

from filters.chat_types import ChatTypeFilter

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message) -> None:
    await message.answer('Привет! Я виртуальный помощник в нашей пиццерии!')

@user_private_router.message(or_f(Command('menu'), (F.text.lower() == "меню")))
async def menu_cmd(message: types.Message) -> None:
    await message.answer('Вот наше меню:')

@user_private_router.message(F.text.lower() == 'о нас')
@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer('Информация о нас....')

@user_private_router.message((F.text.lower().contains('плат')) | (F.text.lower() == 'способы оплаты'))
@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.Message):
    await message.answer('Способы оплаты: ')

@user_private_router.message((F.text.lower().contains('доставк')) | (F.text.lower() == 'варианты доставки'))
@user_private_router.message(Command('shipping'))
async def shipping_cmd(message: types.Message):
    await message.answer('Варианты доставки: ')