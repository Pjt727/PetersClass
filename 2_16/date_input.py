months: list[str] = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month, day, year = map(int, input("Please eneter your date in format mm/dd/yyyy: ").split('/'))

print(f"The date is: {months[month-1]} {day}, {year}.")
print("The data is: " + months[month-1] + " " + day + ", " + year + ".")