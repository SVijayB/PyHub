# Creating a function to call nested functions and provide data using encapsulation

def outer_function(a):
    def inner_function(b):
        return a + b
    return inner_function

def mainfn(b):
    x = outer_function("Hey, ")
    print(x(b))

name = input("Enter your name : ")
mainfn(name)

input("Press any key to exit ")