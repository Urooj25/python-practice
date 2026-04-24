#A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
import datetime
x = datetime.datetime.now()#module,class then method
print(x)
from datetime import datetime, date
print(datetime.now())#datetime Python ka sabse zyada use hone wala built-in module hai — har real project mein kaam aata hai! 
print(date.today())
#Return the year and name of weekday:
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
print(x.strftime("%A"))   # Friday        (poora din)
print(x.strftime("%a"))   # Fri           (short din)
print(x.strftime("%B"))   # April         (poora mahina)
print(x.strftime("%b"))   # Apr           (short mahina)
print(x.strftime("%d"))   # 24            (date)
print(x.strftime("%m"))   # 04            (month number)
print(x.strftime("%Y"))   # 2026          (poora saal)
print(x.strftime("%y"))   # 26            (short saal)
print(x.strftime("%H"))   # 15            (24-hour)
print(x.strftime("%I"))   # 03            (12-hour)
print(x.strftime("%M"))   # 30            (minutes)
print(x.strftime("%S"))   # 45            (seconds)
print(x.strftime("%p"))   # PM            (AM/PM)
print(x.strftime("%A, %d %B %Y"))     # Friday, 24 April 2026
print(x.strftime("%d/%m/%Y"))         # 24/04/2026
print(x.strftime("%I:%M %p"))         # 03:30 PM
print(x.strftime("%A %I:%M %p"))      # Friday 03:30 PM
import datetime
x = datetime.datetime(2026,4,24)
print(x)
#The strftime() Method
import datetime
x = datetime.datetime(2026,4,24)
print(x.strftime("%I"))