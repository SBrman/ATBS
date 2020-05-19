def spam():
    global eggs
    eggs = 'spam' # this is global

def bcaon():
    eggs = 'bacon' # this is local

def ham():
    print(eggs)    # this is global

eggs = 42
spam()
print(eggs)
