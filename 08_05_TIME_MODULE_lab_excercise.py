import time

print('Unix time is:', time.time())
print('Human time is:', time.localtime(time.time()))
print('Better read time is:', time.asctime(time.localtime(time.time())))

import calendar

print(calendar.month(1989,5))

calendar.setfirstweekday(6)

print(calendar.month(1989,5))

print(calendar.isleap(2000))
print(calendar.calendar(2019))

