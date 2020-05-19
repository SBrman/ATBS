#! python3

##Write a program that opens all .txt files in a folder and searches for any
##line that matches a user-supplied regular expression. The results should
##be printed to the screen.

import re, os, pprint

os.chdir(r'H:\python\files\Quiz')

textFiles = []

for file in os.listdir('.'):

    if file[-4:] == '.txt':
        textFiles += [file]

print('Enter the Regular Expression:')
pattern = input()
userRegex = re.compile(pattern)

for file in textFiles:

    openedFile = open(file, 'r')
    text = openedFile.readlines()
    openedFile.close()
    
    print('\nShowing results for %s file:' %(file))
    
    for i in range(len(text)):        
        mo = userRegex.findall(text[i])
        if len(mo) == 0:
            continue
        else:
            print('%s' %mo + ' Found in line number-'+ str(i))
            print(userRegex.sub(mo[0].upper(),text[i]))

print('Done')
