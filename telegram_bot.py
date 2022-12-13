import telebot
from telebot import types

bot = telebot.TeleBot('5982274359:AAHBxZM7_42LBESOhsL_EnvDm_6b3GAWGOM')
# @bot.message_handler(commands = ['help'])
# def start():
#     markup = types.ReplyKeyboardMarkup()
#     info = types.KeyboardMarkup('Info')
#     markup.add(info)




@bot.message_handler()
def all(message):
    if message.text == "hi":
        mess = f'Hello, <b>{message.from_user.first_name} </b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
    elif message.text == "info":
        mess = {message.from_user}
        bot.send_message(message.chat.id, mess, parse_mode='html')
    else:
        bot.send_message(message.chat.id, "Please, choose another command: \nhi\ninfo")

@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.send_message(message.chat.id, 'Photo added!')

# @bot.message_handler(commands)



bot.polling(none_stop = True)