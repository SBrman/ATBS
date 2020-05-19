#! python3

'''
Using the Clipboard to Read a Text Field
'''

import pyautogui, pyperclip

windowName = pyautogui.prompt('Enter the Window Name to grab text from.',
                              'Window Name?')
window = pyautogui.getWindowsWithTitle(windowName)[0]

if window.isMinimized:
    window.restore()
if not window.isActive:
    window.activate()
pyautogui.click(window.center)
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('ctrl','c')
pyautogui.sleep(0.5)
text = pyperclip.paste()

if text != '':
    pyautogui.alert('Text copied to clipboard.')
