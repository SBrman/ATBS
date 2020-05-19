#! python3

import pyautogui, subprocess, time

paint = subprocess.Popen('c:\\Windows\\System32\\mspaint.exe')
time.sleep(1)

p = pyautogui.position()
pyautogui.click(p.x, p.y, button='left')

def colorSelector(number):
    
    change = 40-number
    row_2 = 0
    
    if number > 9:
        number -= 10
        row_2 = 1
        
    pyautogui.moveTo(763+22*number, 62+(row_2*20), duration=0.25)
    pyautogui.click()

    return change
    
for color in range(20):
    distance = 700
    change = colorSelector(color)

    pyautogui.moveTo(400, 200+(1*color))

    while distance > 0:
        
        pyautogui.drag(distance, 0)#, duration=(distance/1000))
        pyautogui.drag(0, distance)#, duration=(distance/1000))
        distance -= change
        pyautogui.drag(-distance, 0)#, duration=(distance/1000))
        pyautogui.drag(0, -distance)#, duration=(distance/1000))
        distance -= change
