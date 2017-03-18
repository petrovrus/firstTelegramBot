import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    pass

@bot.message_handler(content_types=["text"])
def repeat_message(message):
    bot.send_message(message.chat.id, 'Stop saying "' + message.text + '", please!')

if __name__ == '__main__':
    bot.polling(none_stop=True)
