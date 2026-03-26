import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import router


async def main():
    if not TOKEN:
        print("Xato: BOT_TOKEN topilmadi!")
        return

    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(router)

    print("🚀 Bot iske tústi...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot toqtatıldı.")