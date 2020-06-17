import numpy as np

a = np.array([3,1,9,1,5,3,7,8,9,5])     # One Dimentional array
b = np.array([[1,7,3,4],[9,3,6,1],[9,2,8,1]])   # Two Dimentional array
print("a :" ,a)
print("b :", b)

print("\nAccessing a certain item.")
print("1D : ")
print(a[2])     # Starts with 0
print(a[-1])    # Prints last element
print("2D : ")
print(b[1][2])

print("\nFinding the dimension :")
print(a.ndim,"Dimensional array")
print(b.ndim,"Dimensional array")

print("\nShape (Rows, Column)")
print(b.shape)

print("\nSize(Number of elements)")
print(b.size)

print("\nDatatype :")
print(a.dtype)

print("\nUpdating an array :")
print("1D : ")
print(a)
a[1] = 6
print(a)
print("2D :")
print(b)
b[1][2] = 8
print(b)

print("\nPrinting only fixed values(Read comments) : ")
print("1D : ")
print("a :" ,a)
print(a[:3])
print(a[3:])
print(a[3:8])
print(a[::2])   # Skips a value (prints all the second terms)
print(a[::3])   # Prints only the third value
print(a[2::3])  # Starts from the second step and prints only the third term from then
print(a[8::-2]) # Prints from the reverse direction

print("2D : ")
print("b :\n", b)
print(b[:2,:1])
print(b[:2,:2])
print(b[0,:])   # Prints only the first row
print(b[:,0])   # Prints only the first column

print("\nData Conversions : ")
c = np.array([[1,7,6,4],[2,8.4,7,11],[2,6,4.3,12]],dtype = int)
print("Int : \n",c)
c = np.array([[1,7,6,4],[2,8.4,7,11],[2,6,4.3,12]],dtype = float)
print("Float : \n",c)

print("\n Null Matrix : ")
c = np.zeros([3,4],dtype = int) # By default, values are in float
print(c)

print("\nUnit Matrix : ")
c = np.ones([3,4],dtype = int)
print(c)

print("\nCreating an array with a sequence of numbers :")
c = np.arange(5,70,4)
print(c)
x = 2*((4*2)-1)        
c = np.arange(5,70,x)  # You can use complex equations as well
print(c)
c = np.arange(5,70,0.5) # You can use floating point values as well
print(c)