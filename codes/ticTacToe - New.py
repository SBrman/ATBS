import pyinputplus as pyip
import random

# Printing the Board
def printBoard(board):
    print('')
    print(' ' + board[7] + ' | '+ board[8] + ' | ' + board[9])
    print('---+---+---')
    print(' ' + board[4] + ' | '+ board[5] + ' | ' + board[6])
    print('---+---+---')
    print(' ' + board[1] + ' | '+ board[2] + ' | ' + board[3])
    print('')


# Moves
def moves(turn):
    global choices
    while True:
        if turn == player1:
            #Persons move
            move = pyip.inputNum(min=1, max=9, allowRegexes=[str(i) for i in choices]\
                                 ,blockRegexes=[r'.*'])
        else:
            #Computers move
            move = random.choice(choices)
        choices.remove(move)
        
        if theBoard[move] == ' ':
            theBoard[move] = turn
            break
        else:
            print('This place already has a '+ theBoard[move])
            print('Choose another place: ')


# Winning conditions
def winChecker():

    # horizontal
    for i in range(1,8,3):          
        if theBoard[i] == theBoard[i+1] == theBoard[i+2]:
            return 1 if theBoard[i] == player1 else (2 if theBoard[i] == player2 else 0)
            break

    # vertical
    for i in range(1,4):            
        if theBoard[i] == theBoard[i+3] == theBoard[i+6]:
            return 1 if theBoard[i] == player1 else (2 if theBoard[i] == player2 else 0)
            break

    # cross
    if theBoard[1] == theBoard[5] == theBoard[9]:
        return 1 if theBoard[1] == player1 else (2 if theBoard[1] == player2 else 0)
    if theBoard[3] == theBoard[5] == theBoard[7] == player1:
        return 1 if theBoard[1] == player1 else (2 if theBoard[1] == player2 else 0)
    


# Player selection
def player():
    global player1, player2
    print('Player 1, Enter what you want to play with, x or o:')

    while True:
        player1 = pyip.inputStr(allowRegexes=[r'(X|x|0|O|o)'], blockRegexes = [r'.*'])

        if player1 == 'x':
            player1 == 'X'
            player2 = 'O'
            break
        elif player1 == 'o' or player1 == '0':
            player1 == 'O'
            player2 = 'X'
            break
        else:
            print('Player 1, please enter x or o:')
            continue


while True:
    choices = [1,2,3,4,5,6,7,8,9]
    theBoard = {7: ' ',8: ' ',9: ' ',
                4: ' ',5: ' ',6: ' ',
                1: ' ',2: ' ',3: ' '}
    player()    
    print('Player 1 will play with ' + player1 +
          ' and Player 2 will play with ' + player2 + '.')

    printBoard(theBoard)

    win = 0

    for i in range(9):
        if i%2 == 0:
            print('Player 1 enter where to place '+ player1 + ':' )
            turn = player1
            moves(turn)
        else:
            print('Player 2 enter where to place '+ player2 + ':' )
            turn = player2
            moves(turn)
        printBoard(theBoard)

        if i>=4:
            win = winChecker()
            if win == 1:
                print('Player 1 ('+ player1 + ') won.')
                break
            elif win == 2:
                print('Player 2 ('+ player2 + ') won.')
                break

    if win == 0:
        print('Draw!')
        
    print('\nDo you want to play again? Press y for Yes')
    press = input()
    if press != 'y':
        break
