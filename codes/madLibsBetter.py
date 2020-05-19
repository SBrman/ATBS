#! python3

import os, re

os.chdir(r'H:\python\files')

file = open('madLibs.txt')
text = file.read()
file.close()

checkRegex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')

for result in checkRegex.findall(text):
    print('\n\n'+text)
    print('Enter an %s:' %(result.lower()))
    replacement = input()
    text = checkRegex.sub(replacement, text, 1)

newtext = text[:text.index('\n')] + ' '+ text[text.index('\n')+1:]
print(newtext)

print('Select filename to save this text to:')
filename = input()

newFile = open('%s.txt' %(filename),'w')
newFile.write(newtext)
newFile.close()
print('Text saved to %s file' %(filename))

