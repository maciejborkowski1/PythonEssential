import math
def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

a = input('Please enter \'a\' integer: ')
b = input('Please enter \'b\' integer: ')
c = input('Please enter \'c\' integer: ')

if not check_int(a) or not check_int(b) or not check_int(c):
    print('Value(s) is not integer, please enter correct value')
    
else:
    a=int(a)
    b=int(b)
    c=int(c)
    
    if a == 0:
        print('\'a\' can\'t equal zero, please enter correct value for \'a\'')
    else:
        delta = pow(b,2) - (4*a*c)

        if delta < 0:
            print('Delta is smaller than zero. There is no solution.')
        elif delta == 0:
            x1 = -b/2*a
            print('Result of equation is: x1 = %f' % (x1))
        else:
            x1 = (-b-math.sqrt(delta))/2*a
            x2 = (-b+math.sqrt(delta))/2*a
            print('Result of equation is: x1 = %f, x2 = %f' % (x1, x2))
    

