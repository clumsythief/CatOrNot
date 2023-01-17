import os

from keras_cat_recognizer import KerasCatRecognizer

directory_cat_name = "cat_images"
#directory_notCat_name = "notCat_images"
directory_horse_name = "horse_images"
directory_people_name = "person_images"
cat_recognizer = KerasCatRecognizer()

def cat_recogn_in_procents():
    count_cats = 0
    count_imgs = 0

    for file_name in os.listdir(directory_cat_name):
        count_imgs += 1
        if cat_recognizer.is_cat(file_name):
            count_cats += 1

    return (count_cats/count_imgs) * 100

def horse_recogn_in_procents():
    count_horses = 0
    count_imgs = 0

    for file_name in os.listdir(directory_horse_name):
        count_imgs += 1
        if cat_recognizer.is_cat(file_name):
            count_horses += 1

    return (1-(count_horses/count_imgs)) * 100

def people_recogn_in_procents():
    count_people = 0
    count_imgs = 0

    for file_name in os.listdir(directory_people_name):
        count_imgs += 1
        if cat_recognizer.is_cat(file_name):
            count_people += 1

    return (1-(count_people/count_imgs)) * 100
