# Vaatii "pillow" packagen
# Kansiot 'demo/' ja 'resize/' samalla kansiotasolla kuin resizer.py
from PIL import Image
import os
import math
import random

path = "demo/" # Alkuperäiset kuvat
p = "resized/" # Mihin laittaa pienet kuvat
k = "demo/" # Kansioiden nimet, johon pienet kuvat laitetaan esim. "fruits/"
dirs = os.listdir(path)

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            imResize = im.resize((224, 224))
            imResize.save('resized/' + item + '_resized.png', 'PNG', quality=90)


def split_train():
    percent_for_split = 0.15
    d = os.listdir(p)
    split_portion = math.floor(len(d) * percent_for_split)
    checked_indexes = []

    for _ in range(split_portion):
        index = random.randint(0, len(d) - 1)
        while index in checked_indexes:
            index = random.randint(0, len(d) - 1)
        checked_indexes.append(index)
        os.replace(p + d[index], "images/test/" + k + d[index])

    for _ in range(split_portion):
        index = random.randint(0, len(d) - 1)
        while index in checked_indexes:
            index = random.randint(0, len(d) - 1)
        checked_indexes.append(index)
        os.replace(p + d[index], "images/validation/" + k + d[index])

resize()
split_train()

