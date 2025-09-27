import os
import asyncio
import logging

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

load_dotenv()

bot = Bot(os.environ.get("TOKEN"))
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.reply(f"Hello!\nYour ID: {message.from_user.id}\nYour Name: {message.from_user.first_name}")


@dp.message(Command("help"))
async def get_help(message: Message):
    await message.answer("Це команда /help")


@dp.message(F.text =="Як справи?")
async def how_are_you(message: Message):
    await message.answer("Ok!")


@dp.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f"ID фото: {message.photo[-1].file_id}")


@dp.message(Command("get_photo"))
async def get_photo(message: Message):
    await message.answer_photo(
        photo="AgACAgIAAxkBAAImJmjX0w9A-JVwttPnKT_uMGHYHeK2AAK0BzIbB5rBSjgnaH5iwXIpAQADAgADeQADNgQ",
        caption="Це твоє фото"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
