#! python3

'''Practice Project Chapter 9(3)

Filling in the Gaps
Write a program that finds all files with a given prefix, such as spam001.txt,
spam002.txt, and so on, in a single folder and locates any gaps in the numbering
(such as if there is a spam001.txt and spam003.txt but no spam002.txt).
Have the program rename all the later files to close this gap.
As an added challenge, write another program that can insert gaps
into numbered files so that a new file can be added.'''

import os, shutil, re

path = 'H:\\python\\files\\practiceProjectChapter_93'
os.chdir(path)
allFiles = list(os.listdir(path))

fileName = re.compile(r'(.*?)(\d+)(.*)', re.IGNORECASE)

# Finds file name
def nameMaker(text):
    mo = fileName.search(text)

    before = mo.group(1)
    number = int(mo.group(2))
    after = mo.group(3)

    return before, number, after

# formats number in 3 digit
def numFormat(number):
    # ternary: result_1 if condition else result_2
    formatted_number = ('00%s'% (number)) if number<10 else \
             (('0%s' %(number)) if number>9 and number<100 else str(number))

    return formatted_number

# prints missing numbers
def findMissing():

    count = 0
    for i in range(1, len(allFiles)+1):
        
        before, number, after = nameMaker(allFiles[i-1])

        checkFile = before + numFormat(i)+ after
        
        if checkFile not in allFiles:
            print(checkFile + ' is missing.')
            count += 1
            
    return count
    
# Renames each File so that there is no gap
def renameFiles():

    if findMissing() == 0:
        print('Renaming not required.')
        return 0

    else:            
        for i in range(1, len(allFiles)+1):

            before, number, after = nameMaker(allFiles[i-1])

            newName = before + numFormat(i)+ after
            
            location = os.path.abspath(allFiles[i-1])

            print(location + ' to ', end ='')
            print(os.path.join(os.path.dirname(location), newName))
            #shutil.move(location, os.path.join(os.path.dirname(location), newName))

    print('Renaming Done.')

    
while True:
        
    print('Press f for Finding files, \n\
Or, r for Renaming all files to remove any gaps,\n\
Or, anything else to to Quit')

    enter = input()

    if enter.lower() == 'f':
        
        count = findMissing()
        if count == 0:
            print('No missing files found.')
        else:
            print('Total %s files are missing.' %(count))
        
    elif enter.lower() == 'r':
        renameFiles()
        
    else:
        print('Quiting...')
        break
    
