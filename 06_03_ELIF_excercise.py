isPizzaOrdered = False
isBigDrinkOrdered = False
isWeekend = True

if not isWeekend and (isPizzaOrdered or isBigDrinkOrdered):
    print('Congratulations, you can order a free burger!')
elif isWeekend:
    print('If you want get free burger, please come back in working days')
else:
    print('You should order a pizza or big drink')
