# Using decorators we can add new attributes to an existing function.

# Without using decorators : 
def add(x,y):   # def add(x,y,z)
    return x+y  #       return x+y+z 

c = add(5,4)    #c = add(5,4,6)
print(c)        #print(c)

# Using decorators : 
def join(function):
    c = int(input("Enter the third integer : "))
    function.data = c
    return function

def add(x,y):
    return x+y + add.data

a = int(input("Enter the first integer : "))
b = int(input("Enter the second integer : "))
join(add)
c = add(a,b)
print(c)

input("Press Enter key to exit ")