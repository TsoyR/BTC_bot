import telebot
import requests
import json
from datetime import datetime


bot = telebot.TeleBot('5940397535:AAEopOdH2h9q6KfWLKt4JWq7Fav2SwM2P6M')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет введите "price" чтобы найти цену BTC')


@bot.message_handler(content_types=["text"])
def get_text(message):
    if message.text.lower() =='price':
        answer = requests.get("https://yobit.net/api/3/ticker/btc_usd")
        sell_price = answer.json()["btc_usd"]["sell"]
        bot.send_message(message.chat.id,f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}")

bot.polling()
