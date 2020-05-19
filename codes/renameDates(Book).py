#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil, os, re

# Create a regex that matches files with the American date format.

datePattern = re.compile(r'''
                             (^.*?)              # All text before date
                             ((0|1)?\d-)         # one of two digits for the month
                             ((0|1|2|3)?\d-)     # one or two digits for the days
                             ((19|20)\d{2})      # four digits for the year
                             (.*$)
                                ''',re.VERBOSE)

os.chdir(r'H:\python\files\renameDates')
allFiles = list(os.listdir())

for file in allFiles:

    mo = datePattern.search(file)

    if mo == None:
        continue
    
    before = mo.group(1)
    month = mo.group(2)
    day = mo.group(4)
    year = mo.group(6)
    after = mo.group(8)

    newName = before + day + month + year + after

    print('Renaming "%s" to "%s"...' %(file, newName))
    shutil.move(file, newName)
