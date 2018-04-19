import os
import telebot

hostname = "google.com"
channel = '@test'
token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

response = os.system('ping ' + hostname)
bot = telebot.TeleBot(token)


if response == 0:
  print(hostname + ' is up!')
else:
  print(hostname + ' is down!')
  bot.send_message(channel, hostname + ' is down!')