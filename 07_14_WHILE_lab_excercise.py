##initialCapital = 20000
##percentCapital = initialCapital
##percent = 0.03
##maxTimeYears = 10
##Year = 0
##
####while Year <= 9:
####    percentCapital = percentCapital * percent + percentCapital
####    print(percentCapital)
####    Year+=1
####
####print(percentCapital - initialCapital)
print('------------------')

initialCapital = 20000
percent = 0.03
maxTimeYears = 10
year=0
capital=initialCapital
while year<maxTimeYears:
    year+=1
    capital=round((1+percent)*capital,2)
    print('after this year:', year,  'you will have:',capital)
else:
    print('the total revenue is', capital-initialCapital)
print('-------------------------------------------------------')
