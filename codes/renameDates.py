#! python3

'''renameDates.py - Renames filenames with American MM-DD-YYYY date
format to European DD-MM-YYYY.'''

import os, re, shutil

dateRegex = re.compile(r'''
                            (\d{1,2})-   # month
                            (\d{1,2})-   # day
                            (\d{4})      # year
                                    ''', re.VERBOSE)

os.chdir(r'H:\\python\\files\\renameDates')

files = list(os.listdir())

for fileName in files:
    
    changedDateName = dateRegex.sub(r'\2-\1-\3',str(fileName))
    
    if len(changedDateName) == 0:
        continue
    else:
        print('Renaming %s to %s' %(fileName, changedDateName))
        shutil.move(fileName, changedDateName)

