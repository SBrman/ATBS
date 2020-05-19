#! python3

def printPicnic(itemsDict, leftwidth, rightwidth):
    print('\n'+'PICNIC ITEMS'.center(leftwidth+rightwidth, '-'))

    for k,v in itemsDict.items():
        print(k.ljust(leftwidth,'.')+str(v).rjust(rightwidth,' '))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

printPicnic(picnicItems,12,5)
printPicnic(picnicItems,20,6)
