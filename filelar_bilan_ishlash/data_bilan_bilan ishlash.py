# from datetime import date, datetime
# import time

# timestamp = time.time()

# print("timestamp", timestamp)

# d = date.fromtimestamp(timestamp)
# print(d)

# today = date.today()
# todays_info = datetime.now()
# print(todays_info)

# print(today)
# print(today.year)
# print(today.month)
# print(today.day)
# my_date = date(2020, 12, 25)

# print(my_date)

import calendar

# print(calendar.MONDAY)
# print(calendar.calendar(2026))
# print(calendar.calendar(2020, w=4, l=2, c=10, m=12))
# calendar.prcal(2020)
# print(calendar.month(2020, 11))
# calendar.prmonth(2020, 11)
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.month(2025, 11))