import telebot
from telebot import types

from cat_recognizer import CatRecognizer

bot = telebot.TeleBot('5982274359:AAHBxZM7_42LBESOhsL_EnvDm_6b3GAWGOM')


def download_photo(message):
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    with open('image.jpg', 'wb') as new_file:
        new_file.write(downloaded_file)


class AlwaysFalseRecognizer(CatRecognizer):
    def is_cat(self, image_path: str) -> bool:
        return False

cat_recognizer = AlwaysFalseRecognizer()

@bot.message_handler(content_types=['photo'])
def photo(message):
    download_photo(message)
    file_name = 'image.jpg'
    bot.send_message(message.chat.id, cat_recognizer.is_cat(file_name))


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Hello\nWhat do you want to do?\n'
                                      '- /statistics\n'
                                      '- /help</b>', parse_mode = 'html')

@bot.message_handler(commands=['statistics'])
def statistics(message):
    bot.send_message(message.chat.id, '<b>You haven\'t sent a photo yet</b>', parse_mode = 'html')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, open('help_cmd_text.txt', 'r', -1, 'utf-8').read(), parse_mode ='html')

@bot.message_handler()
def all(message):
    if message.text == 'hi':
        mess = f'Hello, <b>{message.from_user.first_name} </b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
    elif message.text == 'info':
        mess = {message.from_user}
        bot.send_message(message.chat.id, mess, parse_mode='html')
    else:
        bot.send_message(message.chat.id, 'Please, choose another command: \nhi\ninfo')

bot.polling(none_stop = True)