import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Naive local time {}".format(local_time))
print("Naive UTC {}".format(utc_time))

aware_local_time = pytz.utc.localize(utc_time).astimezone() # .astimezone() gets the local time zone
aware_utc_time = pytz.utc.localize(utc_time)

print("Aware local time{}, time zone {}".format(aware_local_time, aware_local_time.tzinfo))
print("Aware UTC {}, time zone {}".format(aware_utc_time, aware_utc_time.tzinfo))
# local and UTC time are the same.


gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp()) #1445754600.0 time in seconds

s = 1445733000
t = s + (60 * 60)
gb = pytz.timezone('GB')
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb) #before daylight savings time
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print("{} seconds since the epoch is {}".format(s, dt1))
print("{} seconds since the epoch is {}".format(s, dt2))

# Always convert local time zones to UTC, it's much easier to convert