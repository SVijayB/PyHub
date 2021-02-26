from datetime import *
from dateutil import *
from dateutil.relativedelta import *
from dateutil.parser import * 
import pendulum


print("Right now it is : ", datetime.now())
print("The Date today is : ", date.today())
print(datetime.now() + relativedelta(months=+1))
print(datetime.now() + relativedelta(years = 17,months=+1, weeks=+1))

dt = pendulum.datetime(2021, 2, 25)
print(isinstance(dt, datetime))
pendulum.datetime(2020, 2, 25, tz='Europe/Paris')
dt = pendulum.local(2020,2, 25)
now_in_london = pendulum.now('Europe/London')
print(now_in_london.timezone_name)

print(pendulum.now())
print(pendulum.today())
print(pendulum.yesterday())
print(print(pendulum.tomorrow()))

print(pendulum.parse('2020-02-25T21:00:00'))
print(pendulum.parse('31-01-01', strict=False))

first = pendulum.datetime(2012, 9, 5, 23, 26, 11, 0, tz='America/Toronto')
second = pendulum.datetime(2012, 9, 5, 20, 26, 11, 0, tz='America/Vancouver')
print(first == second)
print (first > second)
print(first <= second)

dt = pendulum.datetime(2021, 2, 26)
print(dt)
dt = dt.add(years=5)
print(dt)
dt = dt.subtract(years=1)
print(dt)