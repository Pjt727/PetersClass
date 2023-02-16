import datetime
month, day, year = map(int, input("Please eneter your date in format mm/dd/yyyy: ").split('/'))
date = datetime.date(year, month, day)

print(f"The date is: {date.strftime('%c')}.")

