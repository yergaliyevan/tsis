from datetime import datetime,timedelta
current=datetime.now()
newday=current-timedelta(days=5)
print(newday)