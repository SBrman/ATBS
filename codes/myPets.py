myPets = ['Zoophie', 'Pooka', 'Fat-tailed']

print('Enter a name')

name = input()

if name not in myPets:
    print(name + ' is not my pet.')
elif name in myPets:
    print(name + ' is my pet.')
    
