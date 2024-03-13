import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

bot = Bot(token="6303439361:AAHwY8EBbWq-1MLfu5noHautpcbvFDDmpK0")
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message) -> None:
    await message.answer('О, привет! Ты нажал на коману СТАРТ!')

@dp.message()
async def echo(message: types.Message) -> None:
    await message.answer(message.text)


async def main() -> None:
    await dp.start_polling(bot)


asyncio.run(main())
