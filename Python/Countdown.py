import datetime

dt  = datetime.datetime
now = dt.now()

# This gives timedelta in days & seconds
dt(year=2016,month=12,day=17) - dt(year=now.year, month=now.month, day=now.day, minute=now.minute)



import datetime

dt=datetime.datetime.now()
mon=12-dt.month
day=17-dt.day
hr=13-dt.hour
mn=60-dt.minute
sec=60-dt.second

print mon,day,hr,mn,sec
