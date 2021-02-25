from datetime import *
from dateutil import parser
from dateutil.relativedelta import *
from dateutil.parser import * 

print (parser.parse('Friday, 26. February 2021 05:52PM')) 
print (parser.parse('2 / 26 / 2021 05:52:26')) 
print (parser.parse('2021-02-26T10:52:26Z'))

print("Right now it is : ", datetime.now())
print("The Date today is : ", date.today())
print(datetime.now() + relativedelta(months=+1))
print(datetime.now() + relativedelta(years = 17,months=+1, weeks=+1))
