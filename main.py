import telebot
import random
from datetime import datetime

bot = telebot.TeleBot(open('bot.txt', 'r').read())

keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.row('Осталось...', 'Давай играть в камень, ножницы, бумага')
keyboard_kmb = telebot.types.ReplyKeyboardMarkup()
keyboard_kmb.row('Камень', 'Ножницы', 'Бумага')



hello = ['привет', 'приветствую']
affairs = ['хорошо', 'нормально']
employ = ['гуляю', 'ем', 'купаюсь', 'сплю', 'с тобой разговариваю', 'играю в БрОуЛь СтАрС', 'играю в Геометри дэш', 'играю в га...ой...в Майнкрафт', 'ничего', 'разговариваю с другим ботом']
months = ["", "январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
kmb = ["камень", "ножницы", "бумага"]

is_kmb_game = False
give_comp = ''
give_user = ''

def el_list(list, el):
    list = list.split()
    for i in list:
        if i == el:
            return True

    return False

def start_kmb(user):
    comp = kmb[random.randint(0, len(kmb) - 1)]
    give_comp = comp
    give_user = user
    if comp == 'камень' and user == 'камень':
        return 'Ничья'

    elif comp == 'камень' and user == 'ножницы':
        return 'Я выйграл'

    elif comp == 'камень' and user == 'бумага':
        return 'Я проиграл'

    elif comp == 'ножницы' and user == 'ножницы':
        return 'Ничья'

    elif comp == 'ножницы' and user == 'бумага':
        return 'Я выйграл'

    elif comp == 'бумага' and user == 'бумага':
        return 'Ничья'



date = datetime.now()
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Это бот созданный специално для 6б класса', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def start_message(message):
    if message.text.lower() == 'давай играть в камень, ножницы, бумага':
        bot.send_message(message.chat.id, 'Камень ножницы бумага раз два три...', reply_markup=keyboard_kmb)
        is_kmb_game = True


    elif message.text.lower() == 'камень':
        bot.send_message(message.chat.id, start_kmb('камень'))
        bot.send_message(message.chat.id, 'Ты дал: ' + give_user + ', а я дал: ' + give_comp)

    elif message.text.lower() == 'ножницы':
        bot.send_message(message.chat.id, start_kmb('ножницы'))
        bot.send_message(message.chat.id, 'Ты дал: ' + give_user + ', а я дал: ' + give_comp)

    elif message.text.lower() == 'бумага':
        bot.send_message(message.chat.id, start_kmb('бумага'))
        bot.send_message(message.chat.id, 'Ты дал: ' + give_user + ', а я дал: ' + give_comp)




    elif el_list(message.text.lower(), 'привет'):
        bot.send_message(message.chat.id, hello[random.randint(0, len(hello) - 1)])

    elif el_list(message.text.lower(), 'дела'):
        bot.send_message(message.chat.id, affairs[random.randint(0, len(affairs) - 1)])

    elif el_list(message.text.lower(), 'делаешь'):
        bot.send_message(message.chat.id, employ[random.randint(0, len(employ) - 1)])

    elif el_list(message.text.lower(), 'времени'):
        bot.send_message(message.chat.id, str(date.hour - 3) + ':' + str(date.minute))

    elif el_list(message.text.lower(), 'дата'):
        bot.send_message(message.chat.id, str(date.day) + '.0' + str(date.month) + '.' + str(date.year))

    elif el_list(message.text.lower(), 'число'):
        bot.send_message(message.chat.id, str(date.day))

    elif el_list(message.text.lower(), 'месяц'):
        bot.send_message(message.chat.id, months[date.month])
    elif el_list(message.text.lower(), 'год'):
        bot.send_message(message.chat.id, str(date.year))

    elif message.text.lower() == 'осталось...':
        now_day = date.day
        now_day + 1
        to_sep = 31 - now_day
        to_sep = to_sep * 24
        hour = date.hour
        to_sep += (24 - hour) - 3
        bot.send_message(message.chat.id, f'Осталось {to_sep} часов...')



bot.polling()
