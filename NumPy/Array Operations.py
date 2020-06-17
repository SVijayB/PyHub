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

print("\nConverting a 1D array into a 2D array : ")
c = np.arange(1,10).reshape(3,3)    # 3 rows and 3 columns
print(c)

print("\nConcatenating Arrays : ")
a = np.arange(0,10,2)
b = np.arange(0,10,3)
c = np.concatenate([a,b])
print(c)
c = c.reshape(3,3)
print("After converting to a 2d array : \n",c)

print("\nComparing elements of two arrays : ")
a = np.array([6,7,3,9])
b = np.array([5,7,9,9])
print(a==b)
print(a>b)

print("\nComparing complete arrays : ")
a = np.array([5,6,7,8])
b = np.array([1,2,3,4])
c = np.array([1,2,3,4])
print(np.array_equal(a,b))
print(np.array_equal(b,c))

print("\nTo add elements at the end of the array : ")
print("a :", a)
print(np.append(a,[100,200,300]))

print("\nGengerating random numbers : ")
big_data = np.random.random_integers(1,100,size=1000)   # Generating 1000 random numbers from 1-100 
print(big_data)