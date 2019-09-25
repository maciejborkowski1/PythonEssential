import random

min=1
max=6

dice = random.randint(min, max)

if dice == 1:
    print('\n','o','\n')
elif dice == 2:
    print(' ','o','\n','\n','o')
elif dice == 3:
    print(' ','','o','\n','','o','','\n','o','','')

print('---------------------')


diceList = []

for i in range (min,max):
    diceList.append(random.randint(min,max))

print(diceList)
