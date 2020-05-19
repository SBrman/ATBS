#! pytjon3

import os, time, datetime, pyperclip

print('Press enter to start the stopwatch and When finished press q or Q and enter.')
input()

startTime = time.time()
dt = datetime.datetime.fromtimestamp(startTime)
dtPretty = dt.strftime('Time- %H:%M:%S %p \t\t\tDate- %d/%m/%I')

text = 'Started stopwatch at:\n%s\n' %dtPretty
print(text)
text += '\n\n'

lapNum = 0
prevTime = startTime

try:
    while True:
        if input().lower() == 'q':
            break
        
        now = time.time()
        lapTime = round(now - prevTime, 2)
        total = round(now - startTime, 2)
        lapNum +=1
            
        text_new = 'Lap #%s:'%(str(lapNum).rjust(3)) +'  '+ (str(lapTime)).rjust(5)\
                                          + '  ' + '(%s)' %((str(total)).rjust(6))
        print(text_new, end='')

        text += text_new + '\n'
        
        prevTime = now

except KeyboardInterrupt:
    pass

text += '\n\n\n'

print('\nStopwatch was stopped.\n')

print('Saving data to H:\\python\\files\\Chapter 17\\Prettified Stopwatch.txt file...')
file = open(r'H:\\python\\files\\Chapter 17\\Prettified Stopwatch.txt', 'a')
file.write(text)
file.close()
print('Lap data saved.\n')
pyperclip.copy(text)
print('Lap data is also copied to clipboard.')
print('\n\nDone.')
