from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import as_list, as_marked_section, Bold

from filters.chat_types import ChatTypeFilter
from keyboards import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message) -> None:
    await message.answer('Привет! Я виртуальный помощник в нашей пиццерии!', reply_markup=reply.start_kb)

@user_private_router.message(or_f(Command('menu'), (F.text.lower() == "меню")))
async def menu_cmd(message: types.Message) -> None:
    await message.answer('Вот наше меню:', reply_markup=reply.del_kb)

@user_private_router.message(F.text.lower() == 'о нас')
@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer('Информация о нас....')

@user_private_router.message((F.text.lower().contains('плат')) | (F.text.lower() == 'способы оплаты'))
@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.Message):
    
    text = as_marked_section(
        Bold("Способы оплаты:"),
        "Картой в боте",
        "При получении (карта/наличные)",
        "В пиццерии",
        marker="✅ "
    )

    await message.answer(text.as_html())

@user_private_router.message((F.text.lower().contains('доставк')) | (F.text.lower() == 'варианты доставки'))
@user_private_router.message(Command('shipping'))
async def shipping_cmd(message: types.Message):
    
    text = as_list(
        as_marked_section(
            Bold("Варианты доставки:"),
            "Курьером",
            "Самовывозом",
            "Поем у вас",
            marker="✅ "
        ),
        as_marked_section(
            Bold("Нельзя:"),
            "Голубями",
            "Почтой",
            marker="❌ "
        ),
            sep='\n---------------------\n'
    )
    await message.answer(text.as_html())