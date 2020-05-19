#! python3

#Finds phone numbers and email addresses on the clipboard.

import re, pyperclip

text = pyperclip.paste()

def phone():
    phonetext = 'PHONE NUMBERS\n'
    
    if phoneNumbers == []:
        phonetext += 'No Phone Number found\n'
    else:
        for phone_index in range(len(phoneNumbers)):
            phonetext += 'Phone Number-' + str(phone_index) + ': ' + phoneNumbers[phone_index][0]+'\n'

    return phonetext

def email():
    emailtext = 'EMAIL IDS\n'
    
    if emailIDs == []:
        emailtext += 'No Email Ids found\n'
    else:
        for email_index in range(len(emailIDs)):
            emailtext += 'Email Id-' + str(email_index) + ': ' + emailIDs[email_index][0]+'\n'
    return emailtext

phoneRegex = re.compile(r'''(
                            \(?\+?88?\)?
                            \s?
                            0
                            \s?
                            1\d
                            \s?
                            \d
                            \s?
                            \d{3,4}
                            \s?
                            \d{3,4}
                            (\s(ext|x|x.|ext.|extension)?\s?d{2,5})?
                            )''', re.VERBOSE)

phoneRegexUS = re.compile(r'''(
                                (\d{3}|\(\d{3}\))? # area code
                                (\s|-|\.)? # separator
                                (\d{3}) # first 3 digits
                                (\s|-|\.) # separator
                                (\d{4}) # last 4 digits
                                (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
                                )''', re.VERBOSE)

emailRegex = re.compile(r'''(
                            (\S@\w*\d*)
                            \.\w{2,4}
                            )''', re.I|re.VERBOSE|re.DOTALL)

phoneNumbers = phoneRegexUS.findall(text)
emailIDs = emailRegex.findall(text)
print(len(emailIDs))

startingMessage = '\n'+ str(len(phoneNumbers)) + ' Phone Numbers found and '\
      +str(len(emailIDs)) + ' Email Ids found.\n\n'

allMessage = startingMessage + phone()+'\n'+ email()
print(allMessage)

pyperclip.copy(allMessage)
print('Everything copied to clipboard')
