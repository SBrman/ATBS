#! python3

'''USAGE -- pdfEncrypt [Lock/Unlock] [password] [path]
'''
import PyPDF2, os, sys, send2trash, time

path = ' '.join(sys.argv[3:])
password = sys.argv[2]

def encryptit():
    for folder, subfolders, files in os.walk(path):
        for file in files:
            if file.endswith('.pdf'):
                filePath = os.path.join(folder, file)
                
                theFile = open(filePath, 'rb')
                pdf = PyPDF2.PdfFileReader(theFile)
                writer = PyPDF2.PdfFileWriter()
                if not pdf.isEncrypted:
                    for pageNum in range(pdf.numPages):
                        page = pdf.getPage(pageNum)
                        writer.addPage(page)

                    newPdfName = os.path.basename(filePath)
                    newPdfName = newPdfName.replace('.pdf', '_encrypted.pdf')
                    newPath = os.path.join(os.path.dirname(filePath), newPdfName)                       
                    new = open(newPath, 'wb')
                    
                    writer.encrypt(password)
                    writer.write(new)
                    new.close()

                    textFile = open(r'H:\python\Passwords\passwords_for_locking_pdfs.txt','a')
                    textFile.write('Time: %s\nFile: %s\nPassword: %s\n\n' %(time.asctime(), newPath, password))
                    textFile.close()

                    theFile.close()

                    send2trash.send2trash(filePath)

    textFile = open(r'H:\python\Passwords\passwords_for_locking_pdfs.txt','a')
    textFile.write('-'*40+'0'+'-'*40+'\n\n')
    textFile.close()
    
              
    return 'Done.'


def decryptit():
    for folder, subfolders, files in os.walk(path):
        for file in files:
            filepath = os.path.join(folder, file)
            theFile = open(filepath, 'rb')
            pdf = PyPDF2.PdfFileReader(theFile)

            if pdf.isEncrypted:
                try:
                    pdf.decrypt(password)
                except:
                    print('File: %s in Path: %s was not decrypted by this password'\
                          %(file, filepath))
                    continue

                writer = PyPDF2.PdfFileWriter()
                for page in range(pdf.numPages):
                    writer.addPage(pdf.getPage(page))


                new = open(os.path.join(os.path.dirname(filepath),\
                        os.path.basename(file).replace('_encrypted.pdf','.pdf')),'wb')
                writer.write(new)
                new.close()
                theFile.close()
                
                send2trash.send2trash(filepath)

    return 'Done'


    
choice = {'lock': encryptit, 'unlock': decryptit}
print(choice[sys.argv[1].lower()]())
