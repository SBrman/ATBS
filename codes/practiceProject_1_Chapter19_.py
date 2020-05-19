#! python3

import os
from PIL import Image

os.chdir(r'H:\python\files\Chapter 19')
os.makedirs(r'.\Project_1', exist_ok=True)

logo = Image.open('catlogo.png')
logoW, logoH = logo.size
logosize = 5

for file in os.listdir('.'):
    if not file.lower().endswith(('png','jpeg','jpg','bmp','gif')) or file == 'catlogo.png':
        continue

    img = Image.open(file)
    im = img.copy()
    imW,imH = img.size

    if (imW/logoW) < 2 or (imH/logoH) < 2:
        continue
        
    print('Resizing logo...')
    logo = logo.resize((logoW,logoH))

    im.paste(logo, (imW-logoW, imH-logoH), logo)

    print('Saving pasted picture...')
    im.save('.\\Project_1\\%s' %(file))
