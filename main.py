import asyncio
from aiogram import types
import logging
from handlers.start import start_router
from handlers.bot import bot, dp
from handlers.shop import shop_router


dp.include_router(start_router)
dp.include_router(shop_router)
async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Начало")
    ])
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())