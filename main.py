import telebot
from telebot import types

bot = telebot.TeleBot('5982274359:AAHBxZM7_42LBESOhsL_EnvDm_6b3GAWGOM')
# @bot.message_handler(commands = ['help'])
# def start():
#     markup = types.ReplyKeyboardMarkup()
#     info = types.KeyboardMarkup('Info')
#     markup.add(info)
from tensorflow import keras
import numpy as np
import cv2

model = keras.applications.VGG16()

img_dir = 'image_dir/HERE_PUT_IMAGE_AND_NAME_IT_LIKE_THIS.jpeg'


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