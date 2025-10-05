from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Каталог")],
        [KeyboardButton(text="Корзина"), KeyboardButton(text="Контакти")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Оберіть варіант"
)

settings = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="YouTube", url=f"https://youtube.com/")]
    ]
)

cars = ["VW", "Fiat", "DMC"]

async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, url=f"https://youtube.com/"))
    return keyboard.adjust(2).as_markup()
