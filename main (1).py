import calendar
yr=int(input("enterthe year:"))
if calendar.isleap(yr):
  print(yr,"is aleap year")
else:
  print(yr,"is not a leap year")
  