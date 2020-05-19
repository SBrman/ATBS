#! python3

'''sendDuesReminders.py - Sends emails based on payment status in spreadsheet.'''

import smtplib, openpyxl, os, pprint

file_path = r'H:/python/files/Chapter 18/duesRecords.xlsx'
wb = openpyxl.load_workbook(file_path)
ws = wb.active

people = {}
''' people = {'name':
                {
                 'email': email,
                 'Dues': ['apr' , 'mar',]
                },
              ...
             }
                
'''

##smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
##smtpObj.ehlo()
##smtpObj.starttls()
##smtpObj.login('@gmail.com', input('Password: '))

def sendEmail(person, months):
    print('Emailing %s for the %s dues\n' %(person, ', '.join(months)))

    message = 'Subject: %s dues unpaid.\nDear %s,\n\nRecords show that you have not\
 paid dues for %s. Please make this payment as soon as possible. Thank you!\n\nBest,\
\nRoach' %(len(months), person, ', '.join(months))

    print('@gmail.com ', people[person]['email'],'\n', message )

##    sendMail = smtpObj.sendmail('@gmail.com ', people[person]['email'], ' ', message)
##    if sendmail  == {}:
##        return 1
##    else:
##        return 0
    

for r in range(2, ws.max_row+1):

    name = ws['A'+str(r)].value
    email = ws['B'+str(r)].value
    
    people.setdefault(name, {'email': email, 'dues':[]})

    for col in range(3, ws.max_column+1):
        if not ws.cell(row=r,column=col).value == 'paid':
            people[name]['dues'].append(ws.cell(row=1, column=col).value)

for name in people.keys():
    if people[name]['dues'] != []:
        print('Name: '+ name +' has %s dues' %(len(people[name]['dues'])))
        print('Email: ' + people[name]['email'])
        print('Months: ' + ', '.join(people[name]['dues'])+'\n')

        if sendEmail(name, people[name]['dues']) == 1:
            print('Email sent.')
        else:
            print('Coud not send email.')
        
        print('\n')
        
smtpObj.quit()
