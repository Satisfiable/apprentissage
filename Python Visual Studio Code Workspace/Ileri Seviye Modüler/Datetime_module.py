from datetime import datetime
import locale

print(datetime.now())

right_now = datetime.now()

"""
print(right_now.year)
print(right_now.month)
print(right_now.day)
print(right_now.hour)
print(right_now.minute)
print(right_now.second)
print(right_now.microsecond)
"""

print(datetime.ctime(right_now))

now = datetime.strftime(right_now, "%A") # Weekday
print(now)

now = datetime.strftime(right_now, "%w") # Weekday as a number 0-6, 0 is Sunday
print(now)

now = datetime.strftime(right_now, "%d") # Day of month 0-31
print(now)

now = datetime.strftime(right_now, "%B") # Month name
print(now)

now = datetime.strftime(right_now, "%m") # Month as a number 1-12
print(now)

now = datetime.strftime(right_now, "%Y") # Year
print(now)

now = datetime.strftime(right_now, "%H") # Hour 00-23
print(now)

now = datetime.strftime(right_now, "%M") # Minute
print(now)

now = datetime.strftime(right_now, "%S") # Second
print(now)

now = datetime.strftime(right_now, "%f") # Microsecond
print(now)

now = datetime.strftime(right_now, "%X") # Local version of time
print(now)

now = datetime.strftime(right_now, "%d.%m.%Y")
print(now)

now = datetime.strftime(right_now, "%H %M %S")
print(now)

print(datetime.strftime(right_now, "%A %B %Y"))

locale.setlocale(locale.LC_ALL, "")

print(datetime.strftime(right_now, "%A %B %Y"))

print(datetime.timestamp(right_now)) # Şu anki zamanın saniye cinsinden değeri

second = datetime.timestamp(right_now)
time = datetime.fromtimestamp(second) # Saniye cinsinden bir değeri datetime objesine (YYYY-mm-dd HH:MM:SS) çevirme
print(time)

now = datetime.fromtimestamp(0)
print(now)

date = datetime(2020, 1, 1)
now = datetime.now()

fark = date - now
print(fark)
print(fark.days)
