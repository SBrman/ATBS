name = input('Enter name: ')
age = int(input('Enter age: '))
if name == 'Alice' and age >= 12 and age < 100 :
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo')
elif age > 100 and age <= 2000:
    print('You are not Alice, grannie')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire')

