import functools
from functools import partial

print("To create functions :\n"+"def functionname(): \n\tfunctionbody")
print()

def full_name(first="vijay",last="balaji"):
	return(first + last)

print("Without default arguments :" , full_name())
print("With Default arguments :" , full_name(last="S"))
print()

print("Unpacking Arguments :")
def selfie(name,age,job) : 
	print("", name , "\n" , age , "\n" , job)
data = ["Vijay",18,"Nothing"]
selfie(*data)
print()

print("Reducing Functions :")
a = [1,2,3,4,5,6,7]
print("List A :",a)
print("Sum of all elements in A :" ,        #To print in the same line
functools.reduce(lambda a,b : a+b, a))      #Have to import functools to reduce. 
print()

print("Partial Functions :")

def fun(a,b,c,d):
	return a+b+c+d

print("Default Argument passing :" , fun(1,2,3,4))
par = partial(fun,5,6,7)					#Have to import from functools to access.
print("Using Partial Function :" , par(7))
par = partial(fun,6,7)
print("Changing two arguments : " , par(8,9))
input("Press any key to exit ")
