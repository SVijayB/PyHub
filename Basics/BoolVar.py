# Boolean Variables
x = True
print(bool(x))

x = 4 
y = 4
print("X :",x)
print("Y :",y)
print("Is X=Y ? " , bool(x==y))
y = 3
print("Y :",y)
print("Is X=Y ? " , bool(x==y))

print("NOTE : If empty sequence, strings, values, are passed, then bool returns false")

def mod(num):
	return (bool(num%2==0))
	
num = int(input("Enter number to check for even or odd : "))
if(mod(num)):
	print("Even")
else:
	print("Odd")