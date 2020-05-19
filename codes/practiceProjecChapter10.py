import random, logging, traceback


#logging.disable(logging.CRITICAL)
logging.basicConfig(filename=r'H:\python\files\Chapter 10\practice_project_debugging_using_loggingModule.txt', level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program.')


guess = ''
logging.debug('guess = %s' %(guess))



def inputChecker(text):
    if text not in ('heads', 'tails'):
        raise Exception('Not heads or tails.')
    return text



    
while guess not in ('heads', 'tails'):

    logging.debug('Start of while loop')
    print('Guess the coin toss! Enter heads or tails:')
    user_input = input()

    try:
        guess = inputChecker(user_input)
    except:
        errorFile = open(r'H:\python\files\Chapter 10\practice_project_errorFile_using_tracebackModule.txt','a')
        errorFile.write(traceback.format_exc()+'\n\n')
        errorFile.close()
        
    logging.debug('You entered guess = %s' %(guess))

logging.debug('End of the while loop')





toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug('Guess is %s and Toss is %s' %(guess, toss))





toss = 'tails' if toss == 0 else 'heads'
logging.debug('Guess is %s and Toss is %s' %(guess, toss))
assert toss in ('heads','tails'), 'toss must be heads or tails'





if toss == guess:
    print('You got it!')
    logging.debug('[If_1:] Guess is %s and Toss is %s' %(guess, toss))
    
else:
    guesss = ''
    while guesss not in ('heads', 'tails'):
        print('Nope! Guess again!')
        guesss = input()

        try:
            guesss = inputChecker(guesss)
        except:
            errorFile = open(r'H:\python\files\Chapter 10\practice_project_errorFile_using_tracebackModule.txt','a')
            errorFile.write(traceback.format_exc()+'\n\n')
            errorFile.close()

    
    logging.debug('[Else_1:] Guesss is %s and Toss is %s' %(guesss, toss))
    
    if toss == guesss:
        print('You got it!')
        logging.debug('[Else_1: if:] Guess is %s and Toss is %s' %(guesss, toss))
        
    else:
        print('Nope. You are really bad at this game.')
        logging.debug('[Else_1: else:] Guess is %s and Toss is %s' %(guesss, toss))

logging.debug('End of program.')
