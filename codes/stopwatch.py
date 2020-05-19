#! python3

'''stopwatch.py - A simple stopwatch program'''

import time

# Display the program's instructions.
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch.\
Press Ctrl-C to quit.')

input()     #press enter to start
startTime = time.time()
print('Started')
lastTime = startTime
lapNum = 1

try:
    while True:
        prevTime = lastTime
        input()
        lastTime = time.time()
        print('Lap: %s\t\tLaptime: %s\t\tTotalTime: %s'
              %(lapNum, round(lastTime-prevTime,2), round(lastTime-startTime,2)), end='')
        lapNum += 1

except KeyboardInterrupt:
    print('\nDone.')
