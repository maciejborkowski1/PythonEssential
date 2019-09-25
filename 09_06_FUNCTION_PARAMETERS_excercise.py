def DoSmth (action, parameter):
    print('action:', action)
    print('parameter:', parameter)
    return

DoSmth('buy','attention')

print('-------------------------------')

def DoSmth2 (action, *parameter):
    print('action:', action)
    print('parameter:', parameter)
    for element in parameter:
        print('Parameter is:', element)
    return

DoSmth2('buy','attention','another')

print('-------------------------------')

def DoSmth3 (action, what, **parameter):
    print('action:', action)
    print('what', what)
    print('parameter:', parameter)
    for element in parameter:
        print(element,'=',parameter[element])
    return

DoSmth3('buy','shoes', size=43, colour='black', typ='sport')
