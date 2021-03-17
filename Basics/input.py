# The input() function takes an input from the user
a = input("What's your favourite colour? ")
print(a)


# By default, the input is read as a string
# To convert it into integer/float value:

b = int(input("Enter an integer: "))  # Integer
print(b)
print(type(b))  # To verify the datatype

c = input("Enter an integer: ")  # String (default)
c = float(c)  # Float (converted)
print(c)
print(type(b))  # To verify the datatype


# To read multiple input values, we use the split() function
d, e, f = input("Enter three space-separated values: ").split()
print(d)
print(e)
print(f)


end = input("Press Enter key to exit ")
