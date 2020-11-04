import pytz # brings in the Olson tz (time zones) database into Python, solivng Daylight savings issues
import datetime

country = 'Europe/Moscow'

# Checking to see if we successfully installed pytz
tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country, local_time))
print("UTC time is {}".format(datetime.datetime.utcnow()))

for x in pytz.all_timezones:
    print(x)

for x in sorted(pytz.country_names):
    print(x + ": " + pytz.country_names[x])


for x in sorted(pytz.country_names):
    print("{}: {}: {}".format(x, pytz.country_names[x], pytz.country_timezones.get(x)))
    # I replaced pytz.country_timezones[x] with pytz.country_timezones.get(x) b/c some countries
    # listed within the olson of IANA database do not have time zones, so get, brings back only time
    # zones that exist while the former method tried to get something that never existed and errored out.

# time zones are asigned on the internet by the IANA (Internet Assigned Numbers Authority) aka olson database

for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]), end=': ')  # prints: timezone/ country under said timezone
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(zone, local_time))
            # print(pytz.country_timezones[x])
    else:
        # print("No time zones are defined")
         print("\t\t No time zone defined")

# In the long term, the best way to deal with local time is to immedietly convert then to UTC and only
# working with them when displaying them back to the user