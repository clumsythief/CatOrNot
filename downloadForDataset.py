import requests
import time
import os.path

for i in range(1500):
    cats = "https://thiscatdoesnotexist.com/"
    horses = "https://thishorsedoesnotexist.com/"
    people = "https://thispersondoesnotexist.com/"

    # notCats = "https://picsum.photos/512"

    #cats
    response = requests.get(cats)
    response.raise_for_status()
    filename = "cat" + str(i) + ".jpeg"
    completeName = os.path.join("cat_images", filename)
    with open(completeName, 'wb') as file:
        file.write(response.content)

    #horses
    response = requests.get(horses)
    response.raise_for_status()
    filename = "horse" + str(i) + ".jpeg"
    completeName = os.path.join("horse_images", filename)
    with open(completeName, 'wb') as file:
        file.write(response.content)

    #people
    response = requests.get(people)
    response.raise_for_status()
    filename = "person" + str(i) + ".jpeg"
    completeName = os.path.join("person_images", filename)
    with open(completeName, 'wb') as file:
        file.write(response.content)

    time.sleep(1)

 #notCats
    #response = requests.get(notCats)
    #response.raise_for_status()
    #filename = "notCat" + str(i) + ".jpeg"
    #completeName = os.path.join("notCat_images", filename)
    #with open(completeName, 'wb') as file:
    #    file.write(response.content)