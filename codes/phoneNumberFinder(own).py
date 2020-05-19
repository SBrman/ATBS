#! python3

def isPhoneNumber(text):
    if len(text) != 12:
        return False

    for i in range(3):
        if not text[i].isdecimal():
            return False

    if text[3] != '-':
        return False

    for i in range(4,7):
        if not text[i].isdecimal():
            return False

    if text[7] != '-':
        return False

    for i in range(8,12):
        if not text[i].isdecimal():
            return False

    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
chunks = message.split(' ')

for chunk in chunks:
    if isPhoneNumber(chunk):
        print('Phone Number Found: '+ chunk + '.' )

print('Done')
