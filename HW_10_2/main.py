import telebot
import HW4_4

TOKEN = ""
bot = telebot.TeleBot(TOKEN, parse_mode=None)

Number = 0
Greetings = "Привет! \n"

Step = 0
First = ''
Second = ''


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'{Greetings} ')
    Get_Polinom(message)


def Get_Polinom(message):
    global First
    global Second
    global Step
    if Step == 0:
        Step = 1
        bot.send_message(message.from_user.id,
                         f'Введите первый многочлен ')
        bot.register_next_step_handler(message, Get_Polinom)
    elif Step == 1:
        Step = 2
        First = message.text
        bot.send_message(message.from_user.id,
                         f'Введите второй многочлен ')
        bot.register_next_step_handler(message, Get_Polinom)
    elif Step == 2:
        Step = 0
        Second = message.text
        try:
            bot.send_message(
                message.from_user.id, f'{HW4_4.sumPolinom(HW4_4.parsPolinom(First),HW4_4.parsPolinom(Second))}')
        except:
            bot.send_message(message.from_user.id,
                             'Ошбка попробуйте еще раз')
        Get_Polinom(message)


bot.polling()
