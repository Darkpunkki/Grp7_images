# Vaatii "pillow" packagen
# Kansiot 'demo/' ja 'resize/' samalla kansiotasolla kuin resizer.py
from PIL import Image
import os

path = "demo"
dirs = os.listdir(path)

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            print(item)
            im = Image.open(path+item)
            imResize = im.resize((200, 200))
            imResize.save('resized/' + item + '_resized.png', 'PNG', quality=90)


resize()

