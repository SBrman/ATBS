#! python3

'''Practice Project Chapter 9(2)

Deleting Unneeded Files

It’s not uncommon for a few unneeded but humongous files or folders to
take up the bulk of the space on your hard drive. If you’re trying to free up
room on your computer, you’ll get the most bang for your buck by deleting
the most massive of the unwanted files. But first you have to find them.
Write a program that walks through a folder tree and searches for exceptionally
large files or folders—say, ones that have a file size of more than
100MB. (Remember, to get a file’s size, you can use os.path.getsize() from
the os module.) Print these files with their absolute path to the screen.'''

import os, shutil, send2trash

path = 'H:\\BOOKS\\Thesis'

fileDict = {}

for folder, subfolders, files in os.walk(path):

    for file in files:
        fileDict[os.path.join(folder, file)] \
                                      = os.path.getsize(os.path.join(folder, file))

for k,v in fileDict.items():
    if int(v) > 100*1024*1024:
        print('The file %s in \nAboslute path: %s \nis %s megabytes\n\n' \
              %(os.path.basename(k),k,round((v/(1024*1024)),2)))
