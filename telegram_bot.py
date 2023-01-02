import telebot
from telebot import types
from tensorflow import keras
import numpy as np
import cv2
#added comment
model = keras.applications.VGG16()

bot = telebot.TeleBot('5982274359:AAHBxZM7_42LBESOhsL_EnvDm_6b3GAWGOM')
# @bot.message_handler(commands = ['start'])
# def start():
#     markup = types.ReplyKeyboardMarkup()
#     info = types.KeyboardMarkup('Info')
#     markup.add(info)

def download_photo(message):
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    with open('image.jpg', 'wb') as new_file:
        new_file.write(downloaded_file)

def CATorNOT(img_dir):
    img = cv2.imread(img_dir)
    img = cv2.resize(img, (224, 224))
    img = np.array(img)
    x = keras.applications.vgg16.preprocess_input(img)
    x = np.expand_dims(x, axis=0)

    res = model.predict(x)
    res = np.argmax(res)

    if 281 <= res <= 285:
        return True
    else:
        return False

@bot.message_handler(content_types=['photo'])
def photo(message):
    download_photo(message)
    file_name = 'image.jpg'
    bot.send_message(message.chat.id, CATorNOT(file_name))


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
    bot.send_message(message.chat.id, open('myfile.txt', 'r', -1, 'utf-8').read(), parse_mode = 'html')

@bot.message_handler()
def all(message):
    if message.text == 'hi':
        mess = f'Hello, <b>{message.from_user.first_name} </b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
    elif message.text == 'info':
        mess = {message.from_user}
        bot.send_message(message.chat.id, mess, parse_mode='html')
    elif message.text == '/help':
        help(message)
    elif message.text == '/start':
        start(message)
    elif message.text == '/statistics':
        statistics(message)
    else:
        bot.send_message(message.chat.id, 'Please, choose another command: \nhi\ninfo')

bot.polling(none_stop = True)