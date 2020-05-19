def function(parameter):
    for i in range(len(parameter)):
        print(parameter[i], end = '')

        if i == len(parameter)-2:
            print(' and ', end = '')
        elif i != len(parameter)-1:
            print(', ', end = '')
        else:
            print('.')

spam = ['apples', 'bananas', 'tofu', 'cats',1,2,3,1,3,4,3,43,5,3,535,5,5,5,3]
function(spam)
