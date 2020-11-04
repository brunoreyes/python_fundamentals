# When dealing with dates, it is best to use DateTime rather than any of the time functions, even
# though they include the data

import time

print("The epoch on this stestem starts at" + time.strftime('%c', time.gmtime(0)))  #gmtime converts UTC to seconds

print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print("\tDaylight Savings Time is in effect for this location")
    print("\tThe DST timezone is " + time.tzname[1])
    
#strftime means "string for time"
print("Local time is "+ time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print("UTC time is "+ time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()))

# avoid using %Z or %z, %Z has been depricated and won't exist soon, %z is not supported everywhere.

import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())  # now is more precise, allowing to use the current timezone
#now uses .tzinfo to account for time zone and daylight savings time
print(datetime.datetime.utcnow())

# Google believes that having continuity is better than having accurate time