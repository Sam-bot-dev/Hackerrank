# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
calen=(calendar.TextCalendar(firstweekday=6).formatyear(2015))
day , month , year = map(int,input().split())
weekday= calendar.weekday(year,day,month)
day= calendar.day_name[weekday]
print(day.upper())

