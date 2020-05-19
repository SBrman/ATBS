import pyinputplus as pyip

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
    while True:
        move = pyip.inputNum(min=1, max=9)
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
            if theBoard[i] == player1:
                return 1
            elif theBoard[i] == player2:
                return 2
            break

    # vertical
    for i in range(1,4):            
        if theBoard[i] == theBoard[i+3] == theBoard[i+6]:
            if theBoard[i] == player1:
                return 1
            elif theBoard[i] == player2:
                return 2
            break

    # cross
    if theBoard[1] == theBoard[5] == theBoard[9] == player1:
        return 1
    elif theBoard[1] == theBoard[5] == theBoard[9] == player2:
        return 2

    if theBoard[3] == theBoard[5] == theBoard[7] == player1:
        return 1
    elif theBoard[3] == theBoard[5] == theBoard[7] == player2:
        return 2
    


# Player selection
def player():
    global player1, player2
    print('Player 1, Enter what you want to play with, x or o:')

    while True:
        player1 = input()

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
        if i == 9 and win == 0:
            print('Draw!')
    print('')
    print('Do you want to play again? Press y for Yes')
    press = input()
    if press != 'y':
        break
