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

print("\nPrinting only fixed values :")
print(a[:3])
print(a[3:])
print(a[3:8])