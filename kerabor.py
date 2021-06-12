import telebot
import requests
 
 
#bot run (запуск бота , можно запустить , остановить . что-то сделать и запустить снова)
 
token = '1896318204:AAFmAm-A6xkAUKzemwMX7xsUz842aclSpzM'
bot = telebot.TeleBot(str(token))
 
#назначение переменным ссылок на загадки и ответ 
zagadka1 = 'https://wdho.ru/fdf65'
zagadka2 = 'https://wdho.ru/b2dc4'
zagadka3 = 'https://wdho.ru/4f106'
otvet = 'https://wdho.ru/f5f72'
 
#обработка команд start и help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.send_message(message.chat.id, 'Бин, я помогу тебе найти Люцика, но я не знаю, где он сейчас, но помню, где он был !') 
  bot.send_message(message.chat.id, zagadka1) #отправка первой ссылки
 
 
#обработка всех входящих текстовых сообщений, если бот в группе , то он видит только сообщения начинающиеся с "/", 
@bot.message_handler(content_types=['text'])
def echo_all(message):
  
  if message.text == '/2376':   #вместо ответ1 - указать правильный ответ
    #bot.send_message(message.chat.id, 'правильный ответ')
    bot.send_message(message.chat.id, zagadka2)
  
  elif message.text == '/6427':
    #bot.send_message(message.chat.id, 'правильный ответ. Загадка3 :')
    bot.send_message(message.chat.id, zagadka3)
  
  elif message.text == '/127':
    bot.send_message(message.chat.id, 'Увы,Люцик куда-то смылся ,оставив лишь этот след:')
    bot.send_message(message.chat.id, otvet)
  else:  #ответ на все остальные сообщения 
    bot.send_message(message.chat.id, 'Люцика тут не было , ищи лучше!!!')
