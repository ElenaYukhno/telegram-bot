import os
import telebot
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("✅ Я был активным")
    markup.add(btn)
    bot.send_message(message.chat.id,
                     "Рада Вас приветствовать! 💚\n\nЕсли Вы были активны на этой неделе — ставили реакции, писали, делились — нажмите кнопку ниже, и я подарю Вам полезный мини-гайд 🎁",
                     reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "✅ Я был активным")
def send_gift(message):
    with open("gift.docx", "rb") as doc:
        bot.send_document(message.chat.id, doc, caption="Спасибо! Вот ваш подарок недели 🎁")

bot.infinity_polling()