# In python we can:
# Define a function inside another function.
# Pass a function as an argumenet to another function.
# Return a function inside or from another function

# Defining a function inside another function : 

def Outside_function():
    def Inside_Function():
        print("Hey, I am the Inside Function")

    print("Hey, I am the outside Function")
    print("These statemenets are executed before the inside function (Inside function is not called yet)")
    Inside_Function()
    print("This statement is executed after the Inside function(Inside function is called)")

Outside_function()

# Example :
def addition(a,b):
    def add(x,y):
        return x+y
    sum = ("The sum is : " + str(add(a,b)))
    return sum

a = int(input("Enter the first term : "))
b = int(input("Enter the second term : "))
answer = addition(a,b)
print(answer)