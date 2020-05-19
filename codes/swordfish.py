while True:
    print('Who are you?')
    name = input()
    if name != 'simanta':
        continue
    print('Hello Simanta, What is the password? (It is a fish)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted')
