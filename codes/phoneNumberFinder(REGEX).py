#! python3

import pyperclip

def isPhoneNumber(text):
    import re
    phoneNumRegexH = re.compile(r'\s\d{3}-\d{3}-\d{4}\s')
    phoneNumRegexB = re.compile(r'\(\d{3}\)\s\d{3}-\d{4}')
    phoneNumRegexD = re.compile(r'\s\d{3}.\d{3}.\d{4}\s')
    phoneNumRegexS = re.compile(r'\s\d{3}\s\d{3}\s\d{4}\s')

    if phoneNumRegexH.search(text) != None:
        mo = phoneNumRegexH.search(text)
        return mo.group()
    
    elif phoneNumRegexB.search(text) != None:
        mo = phoneNumRegexB.search(text)
        return mo.group()
    
    elif phoneNumRegexD.search(text) != None:
        mo = phoneNumRegexD.search(text)
        return mo.group()
    
    elif phoneNumRegexS.search(text) != None:
        mo = phoneNumRegexS.search(text)
        return mo.group()


message = pyperclip.paste()
count = 0

for i in range(len(message)):
    chunks = message[i:i+14]
    if isPhoneNumber(chunks) != None:
        print('Phone Number found: '+ (str(isPhoneNumber(chunks).strip())).rjust(14) \
              +' (Serial No - '+ str(count) \
              + ') LENGTH = '+ (str(len(isPhoneNumber(chunks).strip()))))
        count += 1
        
    if i == len(message)-1 and count == 0:
        print('No phone number found.')

print('Done')
