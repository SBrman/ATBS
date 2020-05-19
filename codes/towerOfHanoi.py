#! python3

'''
Tower of hanoi
'''
count = 0

def move(FROM, TO):
    global count
    
    #print('Move disc from {} to {}'.format(FROM, TO))
    count += 1
    return count

def hanoi(DiscNum,FROM, HELPER, TO):
    if DiscNum == 0:
        return
    
    hanoi(DiscNum-1, FROM, TO, HELPER)
    move(FROM, TO)
    hanoi(DiscNum-1, HELPER, FROM, TO)

hanoi(17,'A','B','C')
print(count)
