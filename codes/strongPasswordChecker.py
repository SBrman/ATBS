#! python3

# Strong Password Detection
'''Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that is at
least eight characters long, contains both uppercase and lowercase characters,
and has at least one digit. You may need to test the string against multiple
regex patterns to validate its strength.'''

'''
at least 8 chars long
upper and lower case letters
at least one digit
'''
import re

def passEvaluater(password):

    lowerCharRegex = re.compile(r'[a-z]+')
    upperCharRegex = re.compile(r'[A-Z]+')
    numberRegex = re.compile(r'\d+')

    if len(password.strip()) < 8:
        print('Not 8 characters long')
        return 0
        
    elif lowerCharRegex.search(password) == None:
        print('No lowercase characters')
        return 0
        
    elif upperCharRegex.search(password) == None:
        print('No uppercase characters')
        return 0
        
    elif numberRegex.search(password) == None:
        print('No digits')
        return 0
        
    else:
        return 1

while True:
    
    typedPassword = input('Enter Password: ')

    result = passEvaluater(typedPassword)

    if result == 0:
        print('\nWeak Password')
    else:
        print('\nStrong Password')

    again = input('\nEnter q to quit. \n\n')
    if again == 'q':
        break
