import telebot
import random
from datetime import datetime

token = open('token.txt', 'r').read()
bot = telebot.TeleBot(token)

keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.row('Осталось...', 'Рандомное число')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Это бот созданный специално для 6б класса', reply_markup=keyboard)

date = datetime.now()

now_day = date.day
now_day + 1
to_sep = 31 - now_day
to_sep = to_sep * 24
hour = date.hour
to_sep += (24 - hour)



@bot.message_handler(content_types=['text'])
def start_message(message):
    if message.text.lower() == 'осталось...':
        # now = datetime.datetime.today()
        # NY = datetime.datetime(2021,9,1)
        # d = NY-now #  str(d)  '83 days, 2:43:10.517807'
        # mm, ss = divmod(d.seconds, 60)
        # hh, mm = divmod(mm, 60)
        bot.send_message(message.chat.id, f'Осталось {to_sep} часов...')

    elif message.text.lower() == 'рандомное число':
        bot.send_message(message.chat.id, random.random())


bot.polling()