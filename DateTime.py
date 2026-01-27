from datetime import date, time, datetime

today=date.today()
now=datetime.now()
print("Todays date is ",today)
print("\nCurrent date and time is ",now)

print("\nDate commponents", today.year, today.month, today.day)