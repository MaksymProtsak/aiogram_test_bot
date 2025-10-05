from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import F, Router

import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.reply(
        f"Hello!\nYour ID: {message.from_user.id}\n"
        f"Your Name: {message.from_user.first_name}",
        reply_markup= await kb.inline_cars()
    )


@router.message(Command("help"))
async def get_help(message: Message):
    await message.answer("Це команда /help")


@router.message(F.text =="Як справи?")
async def how_are_you(message: Message):
    await message.answer("Ok!")


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f"ID фото: {message.photo[-1].file_id}")


@router.message(Command("get_photo"))
async def get_photo(message: Message):
    await message.answer_photo(
        photo="AgACAgIAAxkBAAImJmjX0w9A-JVwttPnKT_uMGHYHeK2AAK0BzIbB5rBSjgnaH5iwXIpAQADAgADeQADNgQ",
        caption="Це твоє фото"
    )
