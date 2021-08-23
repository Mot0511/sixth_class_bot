import telebot
import random
from datetime import datetime

bot = telebot.TeleBot('1979749823:AAFRk_aUPegdWsQ1Z4qBKB7eIxiHs1qX11U')

keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.row('Осталось...')

hello = ['привет', 'приветствую']
affairs = ['хорошо', 'нормально']

def el_list(list, el):
    list = list.split()
    print(list)
    for i in list:
        if i == el:
            return el

        return 'Не понял'

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Это бот созданный специално для 6б класса', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def start_message(message):
    if el_list(message.text.lower(), 'привет'):
        bot.send_message(message.chat.id, hello[random.randint(0, len(hello) - 1)])

    elif el_list(message.text.lower(), 'дела'):
        bot.send_message(message.chat.id, affairs[random.randint(0, len(affairs) - 1)])

    elif message.text.lower() == 'осталось...':
        date = datetime.now()
        now_day = date.day
        now_day + 1
        to_sep = 31 - now_day
        to_sep = to_sep * 24
        hour = date.hour
        to_sep += (24 - hour) - 3
        bot.send_message(message.chat.id, f'Осталось {to_sep} часов...')



bot.polling()
