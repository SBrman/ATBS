#! python3

'''
resizeAndAddLogo.py - Resizes all images in current working directory to fit
in a 300x300 square, and adds catlogo.png to the lower-right corner.
'''

from PIL import Image, ImageColor
import os

os.chdir(r'H:\python\files\Chapter 19')
os.makedirs('.\\pastedLogo', exist_ok=True)

# The picture's smaller dimension to logo's same dimensions ratio
logoSize = 1/5
# Getting the logo
logo_file = r'catlogo.png'


logo = Image.open(logo_file)
logoW, logoH = logo.size


for file in os.listdir('.'):
    if file == 'catlogo.png':
        continue
    if file.endswith('.png') or file.endswith('.jpg'):
        mainImage = Image.open(file)
        im = mainImage.copy()
        imW, imH = im.size
        
        # Resizing the logo
        if imW < imH:            
            logoH = int((logoH/logoW) * imW * logoSize)
            logoW = int(imW/5)
        elif imH < imW :
            logoW = int((logoW/logoH) * imH * logoSize)
            logoH = int(imH/5)
        else:
            logoW = int(imW/5)
            logoH = int(imH/5)
            
##        print('\nPicture (Width, Height): ({},{})\nLogo (Width, Height): ({},{})'\
##              .format(imW, imH, logoW, logoH))            
        print('Resizing logo...')
        logo = logo.resize((logoW,logoH))

        im.paste(logo, (imW-logoW, imH-logoH), logo)

        print('Saving pasted picture...')
        im.save('.\\pastedLogo\\%s' %(file))

##SQUARE_FIT_SIZE = 300
##LOGOFILE = 'catlogo.png'    #logo filepath
##
##logoIm = Image.open(LOGOFILE)
##logoW, logoH = logoIm.size
##
##for file in os.listdir('.'):
##    if not (file.endswith('.png') or file.endswith('.jpg'))\
##       or file == 'catlogo.png':
##        continue
##
##    mainImage = Image.open(file)
##    im = mainImage.copy()
##    width, height = im.size
##
##    if width > SQUARE_FIT_SIZE or height > SQUARE_FIT_SIZE:
##        if width > height:
##            height = int((height/width) * SQUARE_FIT_SIZE)
##            width = SQUARE_FIT_SIZE
##        else:
##            width = int((width/height) * SQUARE_FIT_SIZE)
##            height = SQUARE_FIT_SIZE
##
##        # Resizing the image
##        print('Resizing the image...')
##        im = im.resize((width, height))
##
##    # Adding the logo
##    print('Adding the logo...')
##    im.paste(logoIm, (width-logoW, height-logoH), logoIm)
##    im.save('.\\pastedLogoBook\\%s' %(file))
    
