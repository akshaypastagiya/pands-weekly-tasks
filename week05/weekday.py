# weekday.py
# This program is to get the todays day
# and display if today is weekend or weekdays
# Aurthor: Akshay Pastagiya

from datetime import datetime

dt = datetime.now()
today = dt.strftime('%a')

if dt.isoweekday() >= 6:
    print("Its is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday")