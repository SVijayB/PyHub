# Accessing and manipulating local time.
import time

seconds = time.time()
local_time = time.ctime(seconds)
print("Local time:", local_time)

x = time.struct_time(
    tm_year=2021,
    tm_mon=1,
    tm_mday=31,
    tm_hour=9,
    tm_min=28,
    tm_sec=56,
    tm_wday=6,
    tm_yday=31,
    tm_isdst=0,
)

seconds = time.time()
curr_time = time.localtime(seconds)
print(curr_time)
print("Current year -> ", curr_time.tm_year)

example = "17 July 2001"
ans = time.strptime(example, "%d %B %Y")
print(ans)

import time

for i in range(1, 6):
    print(i)
    time.sleep(1)
