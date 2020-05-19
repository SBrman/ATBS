#! python3

import pyinputplus as pyip
import random, time

numQ = 10
correct = 0

for question in range(numQ):

    num1 = random.randint(2,9)
    num2 = random.randint(2,9)
    prompt = 'Question-%s: %s x %s ?\n' %(question+1, num1, num2)
    answers = [str(num1*num2), str((num1*num2)+random.randint(1,3)),\
              str((num1*num2)-random.randint(1,3)), str(int((num1*num2)/random.randint(2,3)))]

    
    
    random.shuffle(answers)
    correctAns = answers.index(str(num1*num2))
    
    try:
        print('\n\n'+prompt)
        time.sleep(2)
        
        pyip.inputMenu(answers, allowRegexes=[r'%s'%(num1*num2),'ABCD'[correctAns],'abcd'[correctAns]],\
                       blockRegexes=[('^.*$','Incorrect!')], limit=3, timeout=8, lettered=True)

    except pyip.TimeoutException:
        print('Out of time!')   
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correct += 1

print('\n\nYou scored %s/%s.' %(correct, numQ))
