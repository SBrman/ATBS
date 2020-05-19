while True:
    print('Enter your age:')
    age = input()

    if age.isdecimal():
        break
    else:
        print('Please enter a number for your age.')

print('\n\n')

while True:
    print('Select a new password (letters and number only):')
    newPass = input()

    if newPass.isalnum():
        break
    else:
        print('Passwords can only have letters and numbers.')
