stringA = '+---+---+---+---+'
stringB = '|   |   |   |   |'

for string in range(1,11):
    print(stringA)

print('')

for string in range(1,10):
    if string %2 == 0:
        print(stringB)
    else:
        print(stringA)

print('')

for string in range(1,10):
    print ('x' * string)

print('')

for string in range (1,10):
    if string %2 == 0:
        print (string * 'o')
    else:
        print (string * 'x')
