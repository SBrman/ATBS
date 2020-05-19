#! python3

import re, os, shutil, copy

path = r'H:\python\files\practiceProjectChapter_93 - Copy'
os.chdir(path)
allFiles = []

for folder, subfolders, files in os.walk(path):
    for file in files:
        allFiles += [file]
        
oldAllFiles = copy.deepcopy(allFiles)

def nameMaker(text):

    nameRegex = re.compile(r'(.*?)(\d+)(.*)')
    mo = nameRegex.search(text)

    before = mo.group(1)
    number = int(mo.group(2))
    after = mo.group(3)

    return before, number, after

def createName(before, number, after):
    
    formatNumber = '00%s'%(number) if number < 10 else \
                   ('0%s'%(number) if number > 9 and number < 100 \
                    else '%s'%(number))
                    
    newName = before + formatNumber + after

    return newName

gaps = []

before, number, after = nameMaker(allFiles[0])

while True:
    print('Enter number to insert gap or anything else to finish:')
    num = input()
    
    if num.isdigit():
        nameg = createName(before, int(num), after)
        gaps += [nameg]

    else:
        break

for file in allFiles and gaps:
    
    for i in range(allFiles.index(file), len(allFiles)):
        before, number, after = nameMaker(allFiles[i])
        newName =  createName(before, int(number+1), after)
        allFiles[i] = os.path.join(os.path.dirname(file),newName)

src = [0]*len(allFiles)
des = [0]*len(allFiles)


for i in range(len(allFiles)):
    src[i] = os.path.abspath(oldAllFiles[i])
    des[i] = os.path.abspath(allFiles[i])

for i in range(len(allFiles)):
    print('%s to %s' %(src[i], des[i]))
    shutil.move(r'%s' %src[i], r'%s' %des[i])

