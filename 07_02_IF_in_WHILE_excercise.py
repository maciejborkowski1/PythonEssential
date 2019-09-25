##numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
##
##a = 0
##max = len(numbers)-1
##
##while a < max:
##    print (numbers[a], numbers[a+1])
##
##    if numbers[a] * numbers[a] == numbers[a+1]:
##        print('FOUND')
##
##    a+=1

numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

a = 0
max = len(numbers)-2

while a < max:
    print (numbers[a], numbers[a+1], numbers[a+2])

    if numbers[a] ** 2 == numbers[a+1] and numbers[a+1] ** 2 == numbers[a+2]:
        print('FOUND')

    a+=1
