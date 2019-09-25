minLikes = 500
minShares = 100

numLikes = 400
numShares = 122

if numLikes >= minLikes and numShares >= minShares:
    print('Today we cut all prices! 10% discount for everything')
else:
    print('Not enough count of likes and shares. Try again tommorow')

isPizzaOrdered = True
isBigDrinkOrdered = False
isWeekend = False

if not isWeekend and (isPizzaOrdered or isBigDrinkOrdered):
    print('Congratulations, you can order a free burger!')
else:
    print('You are so close, keep calm and try again!')

diskSize = 140
diskSizeUsed = 101
fileSize = 39

if not fileSize > (diskSize - diskSizeUsed):
    print('File can be downloaded.')
else:
    print('Not enough space at local disk!')
