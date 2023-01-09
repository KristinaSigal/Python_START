import telebot
# 5905126060:AAH00fScAi8yAKyY9zppAIS-n9fA8zgKQyM
bot = telebot.TeleBot(
    "5905126060:AAH00fScAi8yAKyY9zppAIS-n9fA8zgKQyM", parse_mode=None)

Number = 0
Greetings = "Привет! Что выхотите сделать:\n"
Menu = "Выберите действие: \n"\
    "1 - Представить число в двоичном виде \n"\
    "2 - Негафибоначи \n"\
    "3 - RLE шифрование"


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'{Greetings} {Menu}')


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    global Number
    try:
        Number = int(message.text)
        #bot.reply_to(message,f' бинарный вид числа {message.text} : {GetBinaryNumer(Number)} ')
        if Number == 1:
            bot.send_message(message.from_user.id,
                             "Введите число: ")
            bot.register_next_step_handler(message, GetBinaryNumer)
        if Number == 2:
            bot.send_message(message.from_user.id,
                             "Введите число: ")
            bot.register_next_step_handler(message, GetNegaFibonachi)
        if Number == 3:
            bot.send_message(
                message.from_user.id, "Введите сироку для шифрования: ")
            bot.register_next_step_handler(message, GetRLE)
    except Exception:
        bot.reply_to(message, f' Ошибка \n {Menu}')


def GetBinaryNumer(message):
    N = int(message.text)
    result = 0
    i = 0
    while N > 0:
        result = result + N % 2 * 10 ** i
        N = N // 2
        i += 1
    bot.send_message(message.from_user.id,
                     f' бинарный вид числа {message.text} : {result} ')
    bot.send_message(message.from_user.id, Menu)


def GetNegaFibonachi(message):
    N = int(message.text)
    result = [1, 0, 1]
    for i in range(1, N):
        result.insert(0, -result[0] + result[1])
        result.append(result[-1] + result[-2])
    bot.send_message(message.from_user.id,
                     f' негафибоначи для числа {message.text} : {result} ')
    bot.send_message(message.from_user.id, Menu)


def GetRLE(message):
    initial_string = message.text
    char = initial_string[0]
    number_of_Char = 1
    serial_Nuber = 1
    result = ''
    for nC in range(1, len(initial_string)):
        if initial_string[nC] == initial_string[nC - 1]:
            serial_Nuber += 1
        else:
            result = result + f'{serial_Nuber}{initial_string[nC - 1]}'
            serial_Nuber = 1
    result = result + \
        f'{serial_Nuber}{initial_string[len(initial_string) - 1]}'
    bot.send_message(message.from_user.id, f' RLE {message.text} : {result} ')
    bot.send_message(message.from_user.id, Menu)
    # split_Result = re.findall('\d+\D', result)
    # repair_String = ''
    # for clausa in split_Result:
    # 	nChar = int(re.search('\d+', clausa)[0])
    # 	char = re.search('\D', clausa)[0]
    # 	repair_String = repair_String + char * nChar
    # print(repair_String)


bot.polling()
