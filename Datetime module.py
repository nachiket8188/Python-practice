import datetime


# d = datetime.date(2018, 10, 25)
# print(d)
from dateutil.zoneinfo import tzfile

tday = datetime.date.today()
# print(tday)
# print(tday.day)
# print(tday.month)
# print(tday.year)
# print(tday.weekday())
# print(tday.isoweekday())

tday = datetime.date.today()
tdelta = datetime.timedelta(days=7)
# print(tday + tdelta)
# print(tday - tdelta)
bday = datetime.date(2020, 8, 22)
till_bday = bday - tday
# print(till_bday)
t = datetime.time(13, 23, 30)
# print(t)
# print(t.hour)
dt = datetime.datetime(2016, 12, 26, 23, 10, 10)
# print(dt)
# print(dt.time())

dt_today = datetime.datetime.today()  # returns current local time w/o the option of timezone.
dt_now = datetime.datetime.now()  #
dt_utcnow = datetime.datetime.utcnow()
print(dt_today)
print(dt_now)
print(dt_utcnow)