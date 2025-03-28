from PIL import Image
import os

path = "images/"
dirs = os.listdir(path)

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            print(item)
            im = Image.open(path+item)
            imResize = im.resize((200, 200))
            imResize.save('resized/' + item + '_resized.jpg', 'JPEG', quality=90)


resize()

# Kansiot 'images' ja 'resize' samalla kansiotasolla kuin resizer.py
