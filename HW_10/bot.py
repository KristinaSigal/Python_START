import telebot
import model
import var
TOKEN = ""
bot = telebot.TeleBot(TOKEN, parse_mode=None)

Number = 0
Greetings = "Привет! Что выхотите сделать:\n"
Menu = "Выберите действие: \n"\
		"1 - Открыть справочник \n"\
		"2 - Найти телефон \n"\
		"3 - Добавить телефон\n"\

WithardStep = 0
Row = dict()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, f'{Greetings} {Menu}')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	global Number
	try:
		Number = int(message.text)
		if Number==1:
			bot.send_message(message.from_user.id, model.Get_Data())
		if Number==2:
			bot.send_message(message.from_user.id, "Введите фамилию: ")
			bot.register_next_step_handler(message, Get_PhoneNumber)
		if Number==3:
			Withard(message)
	except Exception:
		bot.reply_to(message, f' Ошибка \n {Exception}')

def Get_PhoneNumber(message):
	bot.send_message(message.from_user.id, f' {model.Get_Record(message.text)} ')
	bot.send_message(message.from_user.id, Menu)

def Withard(message):
	global WithardStep
	global Row
	if WithardStep < 5:
		if WithardStep == 0:
			bot.send_message(message.from_user.id, f"Введите данные : ")
		else:
			Row[var.FILDS[WithardStep]] = message.text
		WithardStep += 1
		bot.send_message(message.from_user.id, f"{var.FILDS[WithardStep]}: ")
		bot.register_next_step_handler(message, Withard)
	else:
		bot.send_message(message.from_user.id, f"Добавить в справочник { str(Row)} ? (Y/N)")
		bot.register_next_step_handler(message, Add_Row)

def Add_Row(message):
	global WithardStep
	global Row
	WithardStep = 0
	if message.text == 'Y':
		model.Add(Row)
		bot.send_message(message.from_user.id, f"запись добавлена")
		bot.send_message(message.from_user.id, Menu)
	else:
		bot.send_message(message.from_user.id, Menu)
	Row = dict()

def Start_bot():
	global bot
	bot.polling()

Start_bot()

