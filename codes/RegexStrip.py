#! python3


'''Regex Version of strip()
Write a function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to
strip, then whitespace characters will be removed from the beginning and
end of the string. Otherwise, the characters specified in the second argument
to the function will be removed from the string.'''

import re

def regexStrip(text, method):

    stripRegex = re.compile(r'(\s*)(\S+)(\s*)', re.IGNORECASE)
    methodRegex = re.compile(method)
    
    if method == '':
        mo = stripRegex.search(text)
        return mo.group(2)
    
    elif method == 'lstrip':
        mo = stripRegex.search(text)
        return mo.group(2)+mo.group(3)

    elif method == 'rstrip':
        mo = stripRegex.search(text)
        return mo.group(1)+mo.group(2)

    else:
        mo = methodRegex.sub('', text)
        return mo
    

while True:

    print('Enter the text: ')
    message = input()
    if message == '':
        print('You have to enter a some text.')
        continue
    
    print('Enter the instruction (lstrip or rstrip orspecific characters\
or leave this blank to remove whitespace from both sides: ')
    instruction = input()

    result = regexStrip(message, instruction)
    print('#'+result+'#')
    
    again = input('\nEnter q to quit. \n\n')
    if again == 'q':
        break
