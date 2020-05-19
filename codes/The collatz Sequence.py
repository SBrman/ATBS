# The Collatz Sequence

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return (3 * number + 1)

def takeInput():
    print('Type in a number.')

    while True:    
        try:
            entered = int(input())
            break
    
        except ValueError:
            print('You must enter only an integer')
            continue
    
    return entered

while True:
    spam = takeInput()
    while spam != 1:
        spam = int(collatz(spam))

    print('Run again? Y/N.')
    again = input()
    if again == 'N' or again == 'n':
        break
