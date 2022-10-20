import telebot


bot = telebot.TeleBot('5221618050:AAHpT9tpjRbWzVh0yZ_7K3TSGDSUY35gfCo')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, message.text)






bot.polling(True)