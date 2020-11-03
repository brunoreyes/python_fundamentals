# Date and time have some issues: localization and daylight savings

# Localization represent time and time's format in a particular location

# Daylight savings is country specific

# Before daylight savings was choosen on a spur of the moment, now it's known years in advance.

# Date and time on runs on UTC (Universal Time Coordinated)

# Make sure to store dates in UTC to make it more inclusive for users outside of local timezones



# import time

# print(time.gmtime(0)) # converts the number of seconds to a named tuple

# print(time.localtime()) # converts the time in seconds to the local time

# print(time.time())  # specifices the number of seconds since the first of the first of 1917

# time_here = time.localtime()
# print(time_here) # Output: time.struct_time(tm_year=2020, tm_mon=11, tm_mday=3, tm_hour=10, tm_min=26, tm_sec=57, tm_wday=1, tm_yday=308, tm_isdst=0)
# print("Year:", time_here[0], time_here.tm_year)  # Above is a named tuple, tuples are ordered and can be accessed 
# print("Month:", time_here[1], time_here.tm_mon) # By name (tm_year, tm_mon, tm_mday) or by index number
# print("Day:", time_here[2], time_here.tm_mday)


# BELOW WE HAVE CREATED A TIMER, THAT STARTS AND STOPS WHEN ENTER IS PRESSED GIVING THE USER THE TIME IN BETWEEN.
import time
# from time import time as my_timer  # Not the best practice to rename well-known module like "time"


from time import perf_counter as my_timer  # perfect counter
# perf_counter returns the value (in fractional seconds) of a performance counter, i.e.
# a clock with the highest available resolution to measure a short duration like elapse time (time that has gone by)

from time import process_time as my_timer  # process_time measure how long the CPU takes to complete the task


import random

input("Press enter to start")
wait_time = random.randint(1, 6)  # the random mudle is simple, generating a random int between 1 - 6

time.sleep(wait_time) # sleeps for this amount of time
start_time = my_timer()
input("Press enter to stop")

end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at" + time.strftime("%X", time.localtime(end_time)))  #strftime means "string for time"

print("Your reaction time was {} seconds".format(end_time - start_time)) # the time is the difference of end - start
# Your reaction time was 0.0001010894775390625 seconds