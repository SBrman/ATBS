import os
i = 1
for folder, subfolders, files in os.walk(r'H:\python\files\Delicious'):

    print('The current folder is '+ folder.split(os.path.sep)[-1])

    for subfolder in subfolders:
        print('The subfolder of '+ folder.split(os.path.sep)[-1] + ': ' + subfolder.split(os.path.sep)[-1])

    for file in files:
        print('The file of '+ folder.split(os.path.sep)[-1] + ': ' + file.split(os.path.sep)[-1])

    
    print('\n[Main for loop iteration '+str(i)+' index='+str(i-1)+']\n\n')
    i += 1

    
    
