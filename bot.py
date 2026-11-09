import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, BotCommand

TOKEN = "8869897716:AAG13rX0nbq3DKvpVx7ZrAHa2zx-Xy9xhd0"

bot = Bot(token=TOKEN)
dp = Dispatcher()

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💰 Depozit qilish"), KeyboardButton(text="📊 Balansni tekshirish")],
        [KeyboardButton(text="🎁 Promo-kod olish"), KeyboardButton(text="🌐 Saytga kirish (Silka)")],
        [KeyboardButton(text="📲 Ilovani yuklab olish"), KeyboardButton(text="📞 Admin bilan bog'lanish")]
    ],
    resize_keyboard=True
)

async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command="/start", description="Botni qayta ishga tushirish"),
        BotCommand(command="/help", description="Yordam olish")
    ]
    await bot.set_my_commands(main_menu_commands)

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(
        "👋 Xush kelibsiz! 1Win Cash Agent botiga xush kelibsiz.\n\n"
        "Quyidagi menyudan o'zingizga kerakli bo'limni tanlang:",
        reply_markup=menu_keyboard
    )

@dp.message(lambda message: message.text == "💰 Depozit qilish")
async def deposit_process(message: types.Message):
    await message.answer(
        "📝 **Depozit qilish uchun:**\n\n"
        "1. 1Win ID raqamingizni kiriting.\n"
        "2. To'lov tizimini tanlang va pulni o'tkazing.\n\n"
        "Hozircha hisob to'ldirish uchun 1Win ID raqamingizni yozib qoldiring:"
    )

@dp.message(lambda message: message.text == "📊 Balansni tekshirish")
async def balance_process(message: types.Message):
    await message.answer("💳 Sizning agentlik balansingiz hozirda: 0 UZS")

@dp.message(lambda message: message.text == "🎁 Promo-kod olish")
async def promo_process(message: types.Message):
    await message.answer(
        "🎁 **Siz uchun maxsus 1Win Promo-kod:**\n\n"
        "👉 **Feruz063** 👈\n\n"
        "Ushbu promo-kodni ro'yxatdan o'tishda kiriting va birinchi depozitingiz uchun **+500% bonus** oling!"
    )

@dp.message(lambda message: message.text == "🌐 Saytga kirish (Silka)")
async def link_process(message: types.Message):
    await message.answer(
        "🌐 **1Win Rasmiy saytiga kirish havolasi:**\n\n"
        "👉 [1Win Saytiga o'tish](https://1win.com) \n\n"
        "*(Ushbu havola orqali blokirovkalarsiz to'g'ridan-to'g'ri saytga kira olasiz)*"
    )

@dp.message(lambda message: message.text == "📲 Ilovani yuklab olish")
async def app_process(message: types.Message):
    await message.answer(
        "📲 **1Win rasmiy mobil ilovasini yuklab oling:**\n\n"
        "🤖 [Android uchun yuklash](https://1win.com)\n"
        "🍏 [iOS (iPhone) uchun yuklash](https://1win.com)\n\n"
        "Ilovani o'rnatib, qulay sharoitda pul tiking va yutuqlarni yechib oling!"
    )

@dp.message(lambda message: message.text == "📞 Admin bilan bog'lanish")
async def admin_process(message: types.Message):
    await message.answer(
        "👨‍💻 **Qo'llab-quvvatlash xizmati:**\n\n"
        "Savollar, muammolar yoki takliflar bo'yicha admin bilan bog'lanishingiz mumkin:\n"
        "👉 @feruz063"
    )

async def main():
    await set_main_menu(bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
