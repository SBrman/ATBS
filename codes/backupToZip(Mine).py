#! python3

import os, shutil, zipfile

path = 'H:\\python\\files\\backupToZip\\Delicious'

def newpath(fullpath, current):
    
    new_length = len(fullpath) - len(current)
    new_path = fullpath[-new_length:] + '\\'
    return new_path
    

def backupToZip(folder):

    os.chdir(folder)
    os.chdir('..\\')
    backup_dir = os.getcwd()
    
    number = 1
    while True:
        zipFileName = os.path.basename(folder)+'_'+str(number)+'.zip'

        if not os.path.exists(zipFileName):
            break

        number += 1

    compressedFile = zipfile.ZipFile(zipFileName, 'w')

    for folder, subfolders, files in os.walk(folder):
        
        foldername = list(folder.split(os.path.sep))
        print('Adding files to %s' %(foldername[-1]))
        compressedFile.write(folder, newpath(folder, backup_dir))

        for file in files:
            
            if file.startswith(os.path.basename(folder)+'_') and file.endswith('.zip'):
                continue
            
            print('%s\\%s'%(foldername[-1], file))
            compressedFile.write(os.path.join(folder,file) ,'%s%s'%(newpath(folder, backup_dir),os.path.basename(file)))

backupToZip(path)
