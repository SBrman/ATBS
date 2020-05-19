def eggs(someParameter):
    someParameter.append('Hello!')

def egg(someParameter):
    return someParameter + 'World'

spam = [1,2,3]
vspam = 'Hello '

eggs(spam)
r = egg(vspam)
print(spam)
print(vspam)
print(r)
