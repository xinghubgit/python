import datetime


print(datetime.datetime.today())
print(datetime.timedelta(days=30))


d = datetime.date.today() - datetime.timedelta(days=30)
print(d)