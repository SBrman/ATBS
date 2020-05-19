#! python3

'''
Looking Busy
Many instant messaging programs determine whether you are idle, or away
from your computer, by detecting a lack of mouse movement over some
period of time—say, 10 minutes. Maybe you’re away from your computer but
don’t want others to see your instant messenger status go into idle mode.
Write a script to nudge your mouse cursor slightly every 10 seconds. The
nudge should be small and infrequent enough so that it won’t get in the way
if you do happen to need to use your computer while the script is running.
'''

import time, pyautogui, datetime

windowName = pyautogui.prompt('Enter the Window Name to show your activity.\n\
Scrolls down and up to remain active in a site.',
                              'Window Name?')
timeLimit = str(pyautogui.prompt('Enter the Amount of time to show activity.\n\
(Enter -- <number> h/m/s for hours or minutes or seconds).)', 'Time'))


unit = timeLimit[-1].lower()
t = int(timeLimit[:-2])
if unit == 's':
    dt = datetime.timedelta(seconds=t)
elif unit == 'm':
    dt = datetime.timedelta(minutes=t)
elif unit == 'h':
    dt = datetime.timedelta(hours=t)

window = pyautogui.getWindowsWithTitle(windowName)[0]
start = time.time()
while time.time() < start+dt.seconds:    
    try:
        if window.isMinimized:
            print('Restoring...')
            window.restore()
        if not window.isActive:
            print('Activating...')
            window.activate()
            p = pyautogui.position()
            pyautogui.moveTo(window.center)
            pyautogui.scroll(-10)
            pyautogui.scroll(10)
            pyautogui.moveTo(p)
        else:
            print('Sleeping...')
        time.sleep(3)
    except:
        pyautogui.alert('Stopped the activity showing program.',\
                        'Message from python')
        break
