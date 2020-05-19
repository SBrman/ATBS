#! python3

'''backupToZip.py - Copies an entire folder and its contents into
a ZIP file whose filename increments.'''

import zipfile, os

def backupToZip(folder):
    # Backup the entire contents of "folder" into a ZIP file.

    # geting the absolute path to folder
    folder = os.path.abspath(folder)

    os.chdir(folder)
    os.chdir('..\\')
    
    # checking if file number exists
    number = 1
    
    while True:

        zipFilename = os.path.basename(folder)+ '_' + str(number) + '.zip'

        if not os.path.exists(zipFilename):
            break
        print(number)
        number += 1
        


    # Creating new zip file
    print('Creating %s...' %(zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')


    # Walk the entire folder tree and compress the files in each folder.
    for folder, subfolders, files in os.walk(folder):

        print('Adding files in %s' %(folder))
        backupZip.write(folder)

        for file in files:

            newBase = os.path.basename(file)+'_'
            
            if file.startswith(newBase) and file.endswith('.zip'):
                continue

            backupZip.write(os.path.join(folder,file))

    backupZip.close()
    print('Done.')


backupToZip('H:\\python\\files\\backupToZip\\Delicious')
