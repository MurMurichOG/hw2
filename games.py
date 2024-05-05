from aiogram import F, types, Router
from aiogram.filters import Command

games_router = Router()

@games_router.message(Command("games"))
async def show_categories(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Числа"),
                types.KeyboardButton(text="Орел и решка"),
                types.KeyboardButton(text="Слоты")
            ]
        ]
    )
    await message.answer("Выберите категорию", reply_markup=kb)

@games_router.message(F.text == "Числа")
async def numbers(message: types.Message):
    await message.answer("""Сделайте определенную ставку. Далее вам выпадает число от 1 до 6. Если ваше число больше числа, выпавшего боту - вы выйграли вдвое больше поставленной суммы!""")

@games_router.message(F.text == "Орел и решка")
async def coin(message: types.Message):
    await message.answer("""Сделайте определенную ставку. Далее выберите: орел или решка. Если угадаете - получите свою ставку в удвоенном размере!""")

@games_router.message(F.text == "Слоты")
async def slots(message: types.Message):
    await message.answer("""Сделайте определенную ставку. Далее крутите слоты. Если выпадет три одинаковых числа - вы счастливчик! НО, если вам выпадет три семерки, вы получите свой выйгрыш в УТРОЕННОМ размере!""")
