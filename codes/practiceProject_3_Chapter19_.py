#! python3

import os
from PIL import Image, ImageDraw, ImageFont

os.chdir(r'H:\python\files\Chapter 19')
file = open('guests.txt', 'r')
text = file.read()
guests = text.split('\n')
file.close()

os.makedirs('Project_3', exist_ok=True)

W, H = (4*72*5, 5*72*5)
decoration = Image.open(r'H:/python/files/Chapter 19/Project_3/photo.jpg').convert('RGBA')
decoration = decoration.resize((W, H))

for x in range(W):
    for y in range(H):
        p1, p2, p3, p4 = decoration.getpixel((x,y))
        if (p1>230 and p2>230 and p3>230):
            decoration.putpixel((x,y), (255,255,255,255))

for guest in guests:

    print('Making Invitation for %s...' %(guest))
    img = Image.new('RGBA', (W, H), 'White')

    
    img.paste(decoration, (0,0), decoration)

    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, W, H], outline='Black')

    text = ['It would be a pleasure', 'to have the company of', guest, \
            'at 11010 memory lane','on the evening of', 'April 1st', \
            'at 7 o\'clock']
    color = ['black', 'black', 'purple', 'red', 'black', 'green', 'blue']

    height = 300
    
    for i, (line, color) in enumerate(zip(text, color)):

        fontsize = 100

        if line == guest:
            fontsize = 110
    
        FSMT = ImageFont.truetype('FRSCRIPT.TTF', fontsize)
        textW, textH = draw.textsize(line, FSMT)

        draw.text(((W-textW)/2, height), line, fill=color, font=FSMT)
        height += textH+50
    img.save(r'.\\Project_3\\Invitation for %s.png' %(guest))

print('Done.')
