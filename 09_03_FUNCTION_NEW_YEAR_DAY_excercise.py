def daysToNewYear():

    from datetime import date

    dateToday = date.today()

    currentYear = dateToday.year

    dateEndYear = date(currentYear, 12, 31)

    delta = dateEndYear - dateToday

    print(delta.days)
    return
daysToNewYear()

