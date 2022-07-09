################################################
#                                              #
#          ╭━━━━╮╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭╮        #
#          ┃╭╮╭╮┃╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱╱╱┃┃        #
#          ╰╯┃┃┣┻━┳╮╭┳┳━━┫┃╱╱╭━━┳━╮╭━╯┃        #
#          ╱╱┃┃┃╭╮┣╋╋╋┫╭━┫┃╱╭┫╭╮┃╭╮┫╭╮┃        #
#          ╱╱┃┃┃╰╯┣╋╋┫┃╰━┫╰━╯┃╭╮┃┃┃┃╰╯┃        #
#          ╱╱╰╯╰━━┻╯╰┻┻━━┻━━━┻╯╰┻╯╰┻━━╯        #
#          ╭━━━╮╱╱╱╱╱╱╱╱╭╮                     #
#          ┃╭━╮┃╱╱╱╱╱╱╱╭╯╰╮                    #
#          ┃╰━╯┣━━┳╮╭┳━┻╮╭╋━━╮                 #
#          ┃╭╮╭┫┃━┫╰╯┃╭╮┃┃┃┃━┫                 #
#          ┃┃┃╰┫┃━┫┃┃┃╰╯┃╰┫┃━┫                 #
#          ╰╯╰━┻━━┻┻┻┻━━┻━┻━━╯                 #
#                                              #
#     by: sh4d0w0st1n / https://avatok.tk      #
#                                              #
################################################
import telebot
import os
from telebot import apihelper

token = '5431233296:AAGWTRL3wkeuw30EBfbcFq97azhv6ey536U'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Эй! Тебе сюда нельзя!')

@bot.message_handler(commands=['passwd_dof2552'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Перезапустить сервер', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Выключить сервер', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='Перепаковать конфиг', callback_data=5))
    markup.add(telebot.types.InlineKeyboardButton(text='[!] Очистить Базу Данных', callback_data=6))
    bot.send_message(message.chat.id, text="Выберите функцию:", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'да, я хочу очистить базу данных.':
        bot.send_message(message.chat.id, 'Press F to pay respect!\nБаза данных была очищена!')
        os.system("redis-cli FLUSHDB")
    elif message.text.lower() == 'reboot':
        bot.send_message(message.chat.id, 'OK!')
        os.system("cd /system/malvare\nscreen -S 9 python3 main.py")

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id, text='Выполнено!')
    answer = ''
    if call.data == '3': #Перезапуск сервера
        answer = 'Готово! Сервер перезапущен!'
        os.system('pkill python3.7\npkill python3.7\n')
        os.system('cd /root/new/\npython3.7 web.py & python3.7 server.py')
    elif call.data == '4': #Отключение сервера
        answer = 'Сервер был выключен!'
        os.system('cd /root/new/\n./stop.sh')
    elif call.data == '5': #репак конфига
        answer = 'Конфиг был успешно перепакован!'
        os.system('cd /root/new/utils/\npython3.7 repack_config.py')
    elif call.data == '6': #Очистка БД
        answer = 'Для подтверждения выполнения операции, введите: Да, я хочу очистить базу данных.'

    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

bot.polling()