# Function returning another function : 
def outer_function(a):
    def inner_function(b):
        return a + b
    return inner_function

z = outer_function(2)

ans = z(4)  # Accessing the outer_function object(z) to provide value to the inner function

print(ans)

# Example 2 : 
def polynomial(a,b,c):
    def pol(x):
        return (a*x)**2 + b*x + c
    return pol

expression = polynomial(1,2,3)
print(expression(4))

input("Press any key to exit ")