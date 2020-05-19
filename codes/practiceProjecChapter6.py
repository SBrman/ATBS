def printTable(listoflist):
    
    longestWidth = [0] * len(listoflist)
    innerListSize = 0
    
    for i in range(len(listoflist)):
        for j in range(len(listoflist[i])):
            
            if longestWidth[i] < len(listoflist[i][j]):
                longestWidth[i] = len(listoflist[i][j])
                
            if innerListSize < len(listoflist[i]):
                innerListSize = len(listoflist[i])
                
    for i in range(innerListSize):
        for j in range(len(listoflist)):
            print(listoflist[j][i].rjust(longestWidth[j]), end = ' ')
            
        print('')

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
