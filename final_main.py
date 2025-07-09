
import telebot
import os

TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

# Удаляем старый webhook, если он есть
bot.remove_webhook()

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот и готов помочь 💬")

# Запускаем бота в режиме polling
bot.polling(none_stop=True)
