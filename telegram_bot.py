import telebot
from telebot import types

bot = telebot.TeleBot('5982274359:AAHBxZM7_42LBESOhsL_EnvDm_6b3GAWGOM')
# @bot.message_handler(commands = ['start'])
# def start():
#     markup = types.ReplyKeyboardMarkup()
#     info = types.KeyboardMarkup('Info')
#     markup.add(info)




# @bot.message_handler()
# def all(message):
#     if message.text == "hi":
#         mess = f'Hello, <b>{message.from_user.first_name} </b>'
#         bot.send_message(message.chat.id, mess, parse_mode='html')
#     elif message.text == "info":
#         mess = {message.from_user}
#         bot.send_message(message.chat.id, mess, parse_mode='html')
#     else:
#         bot.send_message(message.chat.id, "Please, choose another command: \nhi\ninfo")
#



@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.send_message(message.chat.id, 'CAT EBANYI!')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Hello\nWhat do you want to do?\n'
                                      '- /statistics\n'
                                      '- /help</b>', parse_mode = 'html')

@bot.message_handler(commands=['statistics'])
def start(message):
    bot.send_message(message.chat.id, '<b>You haven\'t sent a photo yet</b>', parse_mode = 'html')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, open('myfile.txt', 'r', -1, 'utf-8').read(), parse_mode = 'html')



bot.polling(none_stop = True)
