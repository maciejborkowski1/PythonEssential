isAutomaticMode = False
is80PercentLight = True
isDirectLight = False
isRainy = True

turnOnLightsOn = isAutomaticMode and not is80PercentLight \
                 or isAutomaticMode and isDirectLight \
                 or isAutomaticMode and isRainy

print('Automatic Mode:  ', isAutomaticMode)
print('Is a good light: ', is80PercentLight)
print('Is sun low:  ', isDirectLight)
print('Is it rainy: ', isRainy)
print('Turn on lights on:   ', turnOnLightsOn)

#rozwiązanie nauczyciela:
#turnLightsOn = isAutomaticMode and (not is80PercentLight or isDirectLight or isRainy)

#opisuj funkcje!!
