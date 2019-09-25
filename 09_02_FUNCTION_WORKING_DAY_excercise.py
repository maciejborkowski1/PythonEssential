from datetime import date
from datetime import timedelta

def PrintCurrentWorkingDay(year=date.today().year, \
                           month=date.today().month, \
                           day=date.today().day):

    day = date(year, month, day)

    if day.weekday() == 5:
        workingDay = day + timedelta(days=2)
    if day.weekday() == 6:
        workingDay = day + timedelta(days=1)
    else:
        workingDay = day

    
    return workingDay


print('Next working day for today is:', PrintCurrentWorkingDay())
