#! python3

'''wordToPdf.py -- Converts word file to pdf file'''

import os, sys, win32com.client, docx, pyperclip

if len(sys.argv) == 2:
    word_address = os.path.abspath(' '.join(sys.argv[1:]))
else:
    word_address = os.path.abspath(pyperclip.paste())

pdf_address = os.path.join(os.path.dirname(word_address), os.path.basename(word_address).replace('.docx','.pdf'))


#File Format = 17 for PDF

print('Converting...')
wordObj = win32com.client.Dispatch('Word.Application')
docObj = wordObj.Documents.Open(word_address)
docObj.SaveAs(pdf_address, FileFormat=17)
docObj.Close()
wordObj.Quit()

print('Done.')
print('Both files can be found here: %s' %(os.path.dirname(pdf_address)))
pyperclip.copy(os.path.dirname(pdf_address))
print('The address of the files is also copied to clipboard.')
