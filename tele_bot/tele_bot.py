import telebot

# ;jgf
bot = telebot.TeleBot('5221618050:AAHpT9tpjRbWzVh0yZ_7K3TSGDSUY35gfCo')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, message.text)



@bot.message_handler(content_types=['text'])
def start(message):
    print('Получил текст')
    bot.send_message(message.chat.id, message.text)
    if message.text == 'жопа':
        print('Пизда рулю')
        int('жопа')






bot.polling(True)