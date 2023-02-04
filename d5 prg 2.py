#display whole year calendar

import calendar

print("full calendar")
print(calendar.calendar(2023))

print("particular month")
print(calendar.month(2022,3))

print("set first day of the week")
calendar.setfirstweekday(calendar.SATURDAY)
print(calendar.month(2022,12))

#prg-display date time

import datetime

a=datetime.datetime.now()
print(a)

sv=a.strftime("%y") #lower case
fv=a.strftime("%y") #upper case

print("year short version" ,sv)
print("year full version",fv)
