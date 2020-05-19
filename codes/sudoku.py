#! python3

import time, pyautogui

sudoku =[[ 5 ,  3 , ' ', ' ',  7 , ' ', ' ', ' ', ' '],
         [ 6 , ' ', ' ',  1 ,  9 ,  5 , ' ', ' ', ' '],
         [' ',  9 ,  8 , ' ', ' ', ' ', ' ',  6 , ' '],
         [ 8 , ' ', ' ', ' ',  6 , ' ', ' ', ' ',  3 ],
         [ 4 , ' ', ' ',  8 , ' ',  3 , ' ', ' ',  1 ],
         [ 7 , ' ', ' ', ' ',  2 , ' ', ' ', ' ',  6 ],
         [' ',  6 , ' ', ' ', ' ', ' ',  2 ,  8 , ' '],
         [' ', ' ', ' ',  4 ,  1 ,  9 , ' ', ' ',  5 ],
         [' ', ' ', ' ', ' ',  8 , ' ', ' ',  7 ,  9 ]]

def drawBoard():

    text = ('#'*25+'  ')*3 +'\n'      # First line
    for row in range(9):
        
        for col in range(10):             # Before numbers row
            if col == 3 or col == 6:
                text += '#  #'+ ' '*7
            else:
                text += '#'+ ' '*7

        # NUmbers row Start
        text += '\n#'                               
        for col in range(9):
            text += ' '*3+ f'{sudoku[row][col]}'+' '*3
            if col == 2 or col == 5:
                text += '#  #'
            else:
                text += '#'
        # Numbers row finished
        text += '\n'
        
        for col in range(10):             # After numbers row
            if col == 3 or col == 6:
                text += '#  #'+ ' '*7
            else:
                text += '#'+ ' '*7
        
        if row == 2 or row == 5:
            text +=('\n'+('#'*25+'  ')*3 +'\n')*2
            
        else:
            text +='\n'+('#'*25+'  ')*3 +'\n'

    text +='\n'

    return text


def possible(row, col, number):
    
    # Vertical check
    for r in range(9):
        if sudoku[r][col] == number:
            return False
        
    # Horizontal check 
    for c in range(9):
        if sudoku[row][c] == number:
            return False

    # 3x3 check
    x = (row//3) * 3
    y = (col//3) * 3
    for r in range(x, x+3):
        for c in range(y, y+3):
            if sudoku[r][c] == number:
                return False

    return True


def solve():
    global sudoku

    for r in range(9):
        for c in range(9):
            if sudoku[r][c] == ' ':
                for n in range(1,10):
                    if possible(r, c, n):
                        sudoku[r][c] = n
                        solve()
                        sudoku[r][c] = ' '
                return

    print('Solved Sudoku:\n')
    print(drawBoard())

solve()
