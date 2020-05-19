catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames)+1) + ' or nothing to stop.')
    
    name = input()

    if name == '':
        break
    else:
        catNames =  catNames + [name]

print('The cat names are: ')

for i in range(len(catNames)):
    print(catNames[i], end = '')

    if i >= len(catNames)-1:
        print('.')
    else:
        print(', ', end = '')
