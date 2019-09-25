from math import *

degree = 360

radian = degree * pi / 180
print('%d degree is %f radian' % (degree, radian))
print('%d degree is %f radian' %(degree, radians(360)))

degree = 45

radian = degree * pi / 180
print('%d degree is %f radian' % (degree, radian))


print('%d degree is %f radian' %(degree, radians(45)))

smallPizzaR = 0.22
bigPizzaR = 0.27
familyPizzaR = 0.38
smallPizzaPrice = 11.50
bigPizzaPrice = 15.60
familyPizzaPrice = 22.00

smallPizzaArea = pi*pow(smallPizzaR,2)
smallPizzaAreav2 = pi*smallPizzaR**2
print('Pole powierzchni małej pizzy wynosi %f m2' % (pi*pow(smallPizzaR,2)))
print('Pole powierzchni dużej pizzy wynosi %f m2' % (pi*bigPizzaR**2))
print('Pole powierzchni familijnej pizzy wynosi %f m2' % (pi*pow(familyPizzaR,2)))

print('Cena za m2 małej pizzy wynosi %f' % (smallPizzaPrice/(pi*pow(smallPizzaR,2))))

math_ls = dir(math) 
print(math_ls)
