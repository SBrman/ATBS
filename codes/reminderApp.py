#! python3

import datetime
import time

today510 = datetime.datetime(2020,5,2,17,10)

while datetime.datetime.now() < today510:
    time.sleep(1)
    
print('Reminder: It is 5:10 PM now.')
