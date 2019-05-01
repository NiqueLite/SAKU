import telebot
import requests

bot = telebot.TeleBot("696784173:AAEL2r-0y_qaYAoYLq7bv6hVlJFZJ-pvKCA")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id,"Я бот который создан для\nСАКУ - Секты Анархо-Коммунистов Украины.\nТы можешь запросить у меня ссылку для подключения к САКУ, правила и другие вещи.")

	bot.send_message(message.chat.id,"Команды:\n/rules (Просмотр правил)\n/chat (Получение ссылки на чат САКУ)\n/stickers (Рекомендируемые стикеры)")

	@bot.message_handler(commands=['rules'])
	def send_welcome(message):
		bot.send_message(message.chat.id,"Правила:\n1. Всё добровольно.\nНикто не может Вами управлять.\n2. Администрация может давать советы,\nно это Ваше дело выполнять их или нет.\n3. Если кто-то решит пойти против системы, \nто группа админов может вынести вердикт.\nВсе нарушения - этические нормы)")

	@bot.message_handler(commands=['chat'])
	def send_welcome(message):
		bot.send_message(message.chat.id,"https://t.me/AnarchistSAKU")

	@bot.message_handler(commands=['stickers'])
	def send_welcome(message):
		bot.send_message(message.chat.id,"https://t.me/addstickers/AnUkraine\nhttps://t.me/addstickers/ancapsticker\nhttps://t.me/addstickers/AnarchyUkraine")

bot.polling()

MAX_RETRIES = 20
url ='http://eutils.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi'

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(max_retries=MAX_RETRIES)
session.mount('https://', adapter)
session.mount('http://', adapter)

r = session.get(url)

def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')