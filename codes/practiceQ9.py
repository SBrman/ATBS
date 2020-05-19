while True:                             # created a loop
    spam = input('Enter a number: ')
    if spam == '1':
        print('Hello')
    elif spam == '2':
        print('Howdy')
    elif spam == 'q':           # added that part
        print('Bye bye!')
        break
    else:
        print('Greetings!')
    
