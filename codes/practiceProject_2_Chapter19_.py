#! python3

import os, threading, openpyxl, time
from PIL import Image

start = time.time()

def imageFolderSearch(drive):
    os.chdir(r'%s:\\' %(drive))
    image_folder = {}
    '''
    image_folder = {
                    'folder_1': {
                                 'Photos": number,
                                 'Non Photos': number
                                }
                    }
    '''
    print('Searching in the %s drive...' %(drive.upper()))
    for folder, subfolders, files in os.walk('.'):
        numPhotoFiles = 0
        numNonPhotoFiles = 0

        for file in files:
            if not file.lower().endswith(('jpg','jpeg','png','bmp','gif')):
                numNonPhotoFiles += 1
                continue
            try:
                img = Image.open(os.path.join(os.path.abspath(folder), \
                                              os.path.basename(file)))
            except:
                print(os.path.basename(file))
                numNonPhotoFiles += 1
                continue
            
            W, H = img.size

            if W < 500 and H < 500:
                numNonPhotoFiles += 1
                continue

            numPhotoFiles += 1

        if numPhotoFiles > numNonPhotoFiles:
            image_folder[os.path.abspath(folder)] = {'Photos': numPhotoFiles,
                                                     'Non Photos': numNonPhotoFiles}

    try:
        wb = openpyxl.Workbook()
        ws = wb.create_sheet(index=0, title='%s' %(drive.upper()))
        
        ws['A1'] = 'Directory'
        ws['B1'] = 'Number of Images Files'
        ws['C1'] = 'Number of Non Image Files'

        print('Writting Excel file for the drive %s...' %(drive.upper()))
        for i, (key, value) in enumerate(image_folder.items(), 2):
            ws['A'+ str(i)] = key
            ws['B'+ str(i)] = value['Photos']
            ws['C'+ str(i)] = value['Non Photos']
        wb.save(r'H:\\python\\files\\Chapter 19\\Project_2\\%s_drive.xlsx' \
                %(drive.upper()))
        print('Searching for Drive %s is finished.' %(drive.upper()))
    except:
        print('Error.')

    return


drives = ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
threads = []

for drive in drives:
    imageFolderSearch(drive)

##for drive in drives:
##    threadObj = threading.Thread(target=imageFolderSearch, args=(drive,))
##    threads.append(threadObj)
##    threadObj.start()
##
##for thread in threads:
##    thread.join()

print('Done.')
print('Total time elapsed ' + str(time.time()-start) + ' seconds.')

