from datetime import datetime
date1 = input("first date: ")
date2 = input("second date: ")
date_format = "%d.%m.%Y"
datetime1 = datetime.strptime(date1, date_format)
datetime2 = datetime.strptime(date2, date_format)
delta = datetime2 - datetime1
difference = delta.total_seconds()
print(difference)