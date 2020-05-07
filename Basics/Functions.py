import functools

print("To create functions :\n"+"def functionname(): \n\tfunctionbody")
print()

def full_name(first="vijay",last="balaji"):
	return(first + last)

print("Without default arguments :" , full_name())
print("With Default arguments :" , full_name(last="S"))
print()

print("Unpacking Arguments : ")
def selfie(name,age,job) : 
	print("", name , "\n" , age , "\n" , job)
data = ["Vijay",18,"Nothing"]
selfie(*data)
print()

print("Reducing Functions : ")
a = [1,2,3,4,5,6,7]
print("List A :",a)
print("Sum of all elements in A :" ,        #To print in the same line
functools.reduce(lambda a,b : a+b, a))      #Have to import functools to reduce. 