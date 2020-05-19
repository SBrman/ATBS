#! python3

import os, shutil, csv

path = r'H:\python\files\Chapter 16\RemoveCsvFileHeaders'
os.chdir(path)
os.makedirs('Backup', exist_ok = True)

files = os.listdir()

for file in files:
    if file.endswith('.csv'):

        print('Removing header from '+ str(os.path.basename(file))+ '...')
        shutil.copy(os.path.abspath(file), os.path.join(path,'Backup',file))
        
        data = []
        csvFile = open(file)
        reader = csv.reader(csvFile)
        for row in reader:
            if reader.line_num == 1:
                continue
            data.append(row)
        csvFile.close()

        csvFile = open(file, 'w', newline='')
        writer = csv.writer(csvFile)
        for row in data:
            writer.writerow(row)
        csvFile.close()

        print('Done.')
