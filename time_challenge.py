# Write a small program to dispaly info on the four clocks whose functions we've looked at:
# i.e. time(), perf_counter(), monotonic(), and process_time().

# Use the documentation for the get_clock_info() function to work out how to call it for each of the clocks.

# time.get_clock_info(name)
# Get information on the specified clock as a namespace object. Supported clock names and the corresponding functions to read their value are:

# 'monotonic': time.monotonic() returns Return the value (in fractional seconds) of a monotonic clock, i.e. a clock
#  that cannot go backwards. The clock is not affected by system clock updates.returning the time as nanoseconds

# 'perf_counter': time.perf_counter() good for measuring time between tasks

# 'process_time': time.process_time() good for measuing CPU task time spent

# 'thread_time': time.thread_time() Return the value (in fractional seconds) of the sum
# of the system and user CPU time of the current thread in nanoseconds

# 'time': time.time()

import time

print("time():\t\t\t",time.get_clock_info('time'))
print("perf_counter():\t",time.get_clock_info('perf_counter')) # higher resolution
print("monotonic():\t",time.get_clock_info('monotonic')) # high resolution
print("process_time():\t",time.get_clock_info('process_time'))

