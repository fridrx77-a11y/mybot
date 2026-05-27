import telebot

TOKEN = "8925229632:AAEJUj61IHMjANMvPmbzV81KuyB5zKjZW0E"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🤖 BOT ISHLAYAPTI!")

print("Bot started...")
bot.polling()
