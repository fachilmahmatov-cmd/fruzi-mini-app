import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# SOZLAMALAR
API_TOKEN = '8266778946:AAGX0NFHpCeQwFW7YuMTP_8NLoy5ElYDiRA'
CHANNELS = ['@fruzicoin', '@FeruzAIuz', '@uzbnexus1']
ADMIN_ID = 8099851107

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Kino bazasi
movie_db = {"1": "BAACAgIAAxkBAA"} 

async def check_sub(user_id):
    for ch in CHANNELS:
        try:
            m = await bot.get_chat_member(chat_id=ch, user_id=user_id)
            if m.status == 'left': return False
        except: return False
    return True

@dp.message_handler(commands=['start'])
async def start(m: types.Message):
    if await check_sub(m.from_user.id):
        await m.answer("Xush kelibsiz! Kino kodini yozing:")
    else:
        btn = InlineKeyboardMarkup(row_width=1)
        for c in CHANNELS:
            btn.add(InlineKeyboardButton(text=f"Obuna bo'lish {c}", url=f"https://t.me/{c[1:]}"))
        btn.add(InlineKeyboardButton(text="Tekshirish ✅", callback_data="check"))
        await m.answer("Bot ishlashi uchun kanallarga a'zo bo'ling:", reply_markup=btn)

@dp.callback_query_handler(text="check")
async def check(c: types.CallbackQuery):
    if await check_sub(c.from_user.id):
        await c.message.delete()
        await c.message.answer("Rahmat! Endi kino kodini yozing.")
    else:
        await c.answer("Hamma kanallarga a'zo bo'lmadingiz! ❌", show_alert=True)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
  
