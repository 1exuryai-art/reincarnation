import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "8315955729:AAHSKWoTabr3Ant3rSUpP0zLwqaJaOyIgIY"
SITE_URL = "https://1exuryai-art.github.io/reincarnation/"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text="ОТКРЫТЬ НАБОР",
            web_app=WebAppInfo(url=SITE_URL)
        )
    )

    with open("cover.png", "rb") as photo:
        bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption="РЕИНКАРНАЦИЯ\n\nОтбор на программу наставничества.",
            reply_markup=keyboard
        )

print("bot started")
bot.infinity_polling(skip_pending=True)
