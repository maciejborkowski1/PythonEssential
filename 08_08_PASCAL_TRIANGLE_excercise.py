numbers = [1]
height = 10
weight = 80
line = ''

for n in numbers:
    line+= '%5d' % (n)

print(line.center(weight))

for i in range (height -1):
    newNumbers = [1]
    position = 0

    while position < len(numbers)-1:
        newNumbers.append(numbers[position] + numbers[position+1])
        position+=1
        
    newNumbers.append(1)
    numbers = newNumbers.copy()
    line = ''
    for n in numbers:
        line+= '%5d' % (n)
    print(line.center(weight))
