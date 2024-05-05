import asyncio
from aiogram import types
import logging
from handlers.start import start_router
from bot import bot, dp
from games import games_router


async def on_startup():
    print('Online!')
async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Начало")
    ])
    dp.include_router(start_router)
    dp.include_router(games_router)
    dp.startup.register(on_startup)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
