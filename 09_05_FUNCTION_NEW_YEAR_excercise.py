from datetime import date

def daysToNewYear(year=date.today().year,month=date.today().month,day=date.today().day):

    dateToday = date(year,month,day)

    currentYear = dateToday.year

    dateEndYear = date(currentYear, 12, 31)

    delta = dateEndYear - dateToday

    
    return delta.days

print('To the end of the year we have only %d days' % (daysToNewYear(2019, 1, 31)))
