while True:

    print('Who are you?')
    name = input()
    if name != 'simanta':
        continue
    else:
        print('Hello Simanta') 
        while True:
            print('What is the password? (It is a fish)')
            password = input()
            if password != 'swordfish':
                print('Wrong Password')
            else:
                break
        break
print('Access granted')
