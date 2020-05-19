birthdays = {'Alice': 'Apr 1','Bob': 'Dec 12' ,'Carol': 'Mar 4'}

while True:
    print('Enter a name (blank to quit):')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I don\'t know '+ name +'\'s birthday.')
        print('What is '+ name + '\'s birthday?')
        bday = input()
        birthdays[name] = bday
        print('Updating database...')
        print(name + '\'s birthday is added to the database')
    print('')
