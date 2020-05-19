#! python3

import random, time

def checkInt():

    while True:
        print('Enter the answer: ')
        number = input()
        if number.isdigit():
            return int(number)
            break
        else:
            print('%s is not an integer. Enter a valid integer.' %(number))

correct = 0

for i in range(10):
    
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    cAns = num1*num2
    
    print('%s. %s x %s' %(i+1, num1, num2))
    time.sleep(1)

    start = time.perf_counter()
    for tries in range(3):

        if time.perf_counter() - start >= 8:
                print('Out of time')
                break
            
        if checkInt() == cAns:
            print('Correct.', end = ' ')
            if time.perf_counter() - start >= 8:
                print('But, out of time.')
            elif time.perf_counter() - start < 8:
                correct += 1
            break
        else:
            print('Incorrect')
            if tries == 2:
                print('Out of tries.')
            
print('\nScore: %s/10' %(correct))
