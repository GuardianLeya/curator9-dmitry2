import telebot

bot = telebot.TeleBot('6271379268:AAHS65mEgencRReAu7XZL5MICReMn2wCFlE')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет', parse_mode='Markdown')


@bot.message_handler(commands=['fat'])
def main(message):
    bot.send_message(message.chat.id, '*Ты жирный*', parse_mode='Markdown')


@bot.message_handler(commands=['vertigo'])
def main(message):
    bot.send_message(message.chat.id, '_Ты поплыл_', parse_mode='Markdown')


bot.infinity_polling()