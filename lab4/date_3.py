from datetime import datetime
data=datetime.now()
newdata=data.replace(microsecond=0)
print(newdata)

