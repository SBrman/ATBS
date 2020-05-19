#! python3

import os
os.chdir(r'H:\python\files')

file = open('madLibs.txt')
text = file.read()
file.close()
newtext = ''

file = open('madLibs.txt', 'a')
i = 0
while i in range(len(text)):
    if text[i].isupper():
        if text[i:i+9] == 'ADJECTIVE':
            print('\nEnter an adjective:')
            adj = input()
            i = i+8  
            newtext += adj
            
        elif text[i:i+4] == 'NOUN':
            print('\nEnter an noun:')
            noun = input()
            i = i+3 
            newtext += noun
            
        elif text[i:i+6] == 'ADVERB':
            print('\nEnter an adverb:')
            adverb = input()
            i = i+5  
            newtext += adverb

        elif text[i:i+4] == 'VERB':
            print('\nEnter an verb:')
            verb = input()
            i = i+3  
            newtext += verb
            
        else:
            newtext += text[i]

    elif text[i]=='\n':
        newtext += ' '
    else:
        newtext += text[i]
    i += 1

file.write('\n' + newtext)
file.close()
