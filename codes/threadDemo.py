#! python

import threading, time


print('Start of the program.')

def takeNap():
    time.sleep(5)
    print('Wake up!')

threadObj = threading.Thread(target=takeNap)
threadObj.start()

print('End of program.')
