# Datetime Module: How to work with Dates, Times, Timedeltas, and Timezones

import datetime
import pytz

# d = datetime.date(2016, 7, 24)
tday = datetime.date.today()
#print(d)
print(tday.day)
print(tday.weekday())
print(tday.isoweekday())

tdelta = datetime.timedelta(days=7)

print(tday - tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2016, 9, 24)

till_bday = bday - tday
print(till_bday.days)
print(till_bday.total_seconds())

t = datetime.time(9, 30, 35, 100000)
print(t)
print(t.hour)

t2 = datetime.datetime(2016, 7, 26, 12, 30, 45, 10000)

tdelta = datetime.timedelta(days=7)
print(t2 + tdelta)
print(t2.time())
print(t2.year)


# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()

# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

# dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)

# print(dt)

# dt_now = datetime.datetime.now(tz=pytz.UTC)

# print(dt_now)

# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

# print(dt_utcnow)

# dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
# print(dt_mtn)

dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
print(dt_mtn.isoformat())
print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'June 06, 2022'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)


# dt_east = pytz.timezone('US/Mountain')

# print(dt_east)
#dt_mtn = mtn_tz.localize(dt_mtn)


#dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))


# print(dt_mtn)

# for tz in pytz.all_timezones:
#     print(tz)

