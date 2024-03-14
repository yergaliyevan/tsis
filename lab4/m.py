from datetime import datetime, timedelta
current=datetime.now()
yesterday=current-timedelta(days=1)
print(current)
print(yesterday)


