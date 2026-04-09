import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8315955729:AAHSKWoTabr3Ant3rSUpP0zLwqaJaOyIgIY"

bot = telebot.TeleBot(TOKEN)

PHOTO_URL = "https://1exuryai-art.github.io/reincarnation/реинкарнация.png"
SITE_URL = "https://1exuryai-art.github.io/reincarnation/"

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton("ОТКРЫТЬ НАБОР", url=SITE_URL)
    )

    bot.send_photo(
        chat_id=message.chat.id,
        photo=PHOTO_URL,
        caption="РЕИНКАРНАЦИЯ\n\nОтбор на программу наставничества.",
        reply_markup=keyboard
    )

print("bot started")
bot.infinity_polling()
