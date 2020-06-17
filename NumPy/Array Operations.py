import numpy as np

a = np.array([3,1,9,1])     # One Dimentional array
b = np.array([[1,7,3,4],[9,3,6,1],[9,2,8,1]])   # Two Dimentional array
print(a)
print(b)

# Accessing a certain item.
# 1D
print(a[2])     # Starts with 0
print(a[-1])    # Prints last element
# 2D
print(b[1][2])

# Finding the dimension :
print(a.ndim,"Dimensional array")
print(b.ndim,"Dimensional array")

# Shape (Rows, Column)
print(b.shape)

# Size(Number of elements)
print(b.size)

# Datatype :
print(a.dtype)