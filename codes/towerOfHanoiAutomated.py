#! python3

'''
Tower of hanoi Automated
'''
import time, pyautogui, subprocess


# Positions of the pillars (in the game) and other coordinates (for windowed 1080p maximized)
turn = {'A': (732,230), 'B': (1122,227), 'C': (1515,226)}
homestart = (805,700)
start = (955,870)
playAgain = (1130,775)
goHome = (1130,885)

# Obs studio
startRecording = (1710,910)


def move(FROM, TO):
    global turn, count, text

    txt = 'MOVE {}: Move disc from {} to {}'.format(count+1, FROM, TO)
    text += txt + '\n'
    print(txt)

    
    pyautogui.moveTo(turn[FROM], duration=0.15)
    pyautogui.click(turn[FROM])
    pyautogui.moveTo(turn[FROM][0], 150, duration=0.05)
    
    pyautogui.moveTo(turn[TO], duration=0.15)
    pyautogui.click(turn[TO])
    pyautogui.moveTo(turn[TO][0], 150, duration=0.05)
    
    count += 1


def hanoi(DiscNum,FROM, HELPER, TO):
    if DiscNum == 0:
        return
    hanoi(DiscNum-1, FROM, TO, HELPER)
    move(FROM, TO)
    hanoi(DiscNum-1, HELPER, FROM, TO)


def playGame(number):
    # x and y are the coordinates on screen where mouse will click
    clicks, x, y = (number-5, 955, 335) if number > 5 else (5-number, 955, 380)

    # Clicks up or down to set the disc number
    for _ in range(clicks):
        pyautogui.click(x,y)

    # Clicks ok
    pyautogui.click(1049,365)

    start = time.time()

    # Gameplay
    hanoi(number,'A','B','C')

    # Writing the moveslist in a file
    file = open(r'G:\Tower Of Hanoi\movesListFor%sDiscs.txt' %(number), 'w')
    file.write(text)
    file.close()
    print('Total moves performed: '+ str(count)+ '\nTime passed: '
          + str(time.time()-start) + 'Seconds.')


# Starting game
gamePath = r'G:/Tower Of Hanoi/Game.exe'
toh = subprocess.Popen(gamePath)
time.sleep(2)

tohWindow = pyautogui.getWindowsWithTitle('Tower Of Hanoi')[0]
obs = pyautogui.getWindowsWithTitle('OBS')[0]

tohWindow.maximize()
time.sleep(1)

obs.activate()
time.sleep(2)
pyautogui.click(startRecording)
time.sleep(2)

tohWindow.activate()
time.sleep(0.5)
pyautogui.click(homestart)
time.sleep(0.5)
pyautogui.click(start)

totalDiscs = [x for x in range(3,11)] 

#for discNum in totalDiscs:
discNum = totalDiscs[-1]
print(discNum)
count = 0
text = ''
playGame(discNum)

time.sleep(5)
pyautogui.click(playAgain)
time.sleep(1)

obs.activate()
time.sleep(1)
pyautogui.click(startRecording) # Stop recording
print('\n'*10)
time.sleep(3)
pyautogui.click(startRecording) # Start recording again
time.sleep(2)
tohWindow.activate()
time.sleep(2)
    

obs.activate()
time.sleep(2)
pyautogui.click(startRecording) # Stop recording
time.sleep(3)
tohWindow.close()

import sys
sys.path.append(r'H:\python\codes')
import textMe
textMe.textMe('All done.')
print('Done.')
