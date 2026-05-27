import telebot

TOKEN = "8925229632:AAEJUj61IHMjANMvPmbzV81KuyB5zKjZW0E"

bot = telebot.TeleBot(TOKEN)

# 🌟 /start command
@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = telebot.types.KeyboardButton("👋 Salom")
    btn2 = telebot.types.KeyboardButton("ℹ️ Info")
    btn3 = telebot.types.KeyboardButton("📞 Help")

    markup.add(btn1, btn2, btn3)

    bot.send_message(
        message.chat.id,
        "🤖 Assalomu alaykum!\n\nMenu dan birini tanla 👇",
        reply_markup=markup
    )

# 👋 Salom button
@bot.message_handler(func=lambda message: message.text == "👋 Salom")
def hello(message):
    bot.send_message(message.chat.id, "👋 Salom do‘stim! Qalaysan 😎")

# ℹ️ Info button
@bot.message_handler(func=lambda message: message.text == "ℹ️ Info")
def info(message):
    bot.send_message(message.chat.id, "🤖 Bu oddiy Telegram bot\n⚡ Python bilan yozilgan")

# 📞 Help button
@bot.message_handler(func=lambda message: message.text == "📞 Help")
def help(message):
    bot.send_message(message.chat.id, "🆘 Yordam kerak bo‘lsa admin yozadi 😁")

# 💬 default reply
@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, "❗ Men faqat menu bilan ishlayman 😅")

bot.polling()
