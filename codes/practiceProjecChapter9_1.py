#! python3

'''Practice Project chapter 9(1)

Selective Copy
Write a program that walks through a folder tree and searches for files with
a certain file extension (such as .pdf or .jpg). Copy these files from whatever
location they are in to a new folder.'''

import os, shutil

path = 'H:\\BOOKS\\Thesis'
newFolder = 'H:\\python\\files\\practiceProjectChapter_91'

for folder, subfolders, files in os.walk(path):
    for file in files:
        if file.endswith('.jpg'):
            print('%s copied to %s.' %(os.path.join(folder, file), newFolder))
            shutil.copy(os.path.join(folder, file), newFolder)
