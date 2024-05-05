from aiogram import Router, types, F
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command("start"))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Получить голду", callback_data="money"),
                types.InlineKeyboardButton(text="Игры", callback_data="games"),
                types.InlineKeyboardButton(text="Курс", callback_data="data")
            ]
        ]
    )
    await message.answer(f"""Привет, {message.from_user.full_name}. Получай голду и играй! """, reply_markup=kb)


@start_router.callback_query(F.data == "money")
async def money(callback: types.CallbackQuery):
    await callback.message.answer_photo(photo="images/photo_5291827474986032000_y.jpg", caption="Проведите оплату")

@start_router.callback_query(F.data == "data")
async def data(callback: types.CallbackQuery):
    await callback.message.answer("""Текущий курс: 1 голда = 0.65 сомов """)
