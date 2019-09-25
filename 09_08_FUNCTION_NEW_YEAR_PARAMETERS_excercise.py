from datetime import date

def daysToNewYear(*dates):
    for dateToday in dates:

        currentYear = dateToday.year

        dateEndYear = date(currentYear, 12, 31)

        delta = dateEndYear - dateToday

        print('Today is', dateToday, 'we have only', delta.days, 'to the end of the year' )
    
    return

daysToNewYear(date(2018,12,1),date(2018,10,12), date.today())
