import numpy as np

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

print("\nLinspace : ")
c = np.linspace(10,100,10)   # From range 10-100 with 10 divisions
print(c)

print("\nPerforming Logical Operations between arrays : ")
a = np.array([0,1,1,0])
b = np.array([1,1,1,0])
print("OR OPERATION  : ",np.logical_or(a,b))
print("AND OPERATION : ",np.logical_and(a,b))
print("XOR OPERATION : ",np.logical_xor(a,b))
print("NOT OEPRATION : ",np.logical_not(a))

print("\nTrignometry Functions : ")
a = np.linspace(0,2,9)
print("a : ", a)
print("COS : \n", np.cos(a))
print("SIN : \n", np.sin(a))
print("TAN : \n", np.tan(a))
print("INVERSE OF SIN : \n", np.arcsin(a))  # Similarly for cos and tan

print("\nMathematical Functions : ")
a = np.array([-1,3,5,-9,10,-7])
print("A : ", a)
b = np.array([6,4,5,5,6,10])
print("B : ", b)
print("Absolute of A : ",np.abs(a))
print("Adding A and B : ", np.add(a,b))
print("Exponents of B : ", np.exp(b))
print("Power of B with base 3 :", np.power(b,3))
print("Log Base 2 of B : ", np.log2(b))
print("Sum of all elements of A : ", np.add.reduce(a))
print("Multiple of all elements of A : ", np.multiply.reduce(a))

print("Finding Maximum and Minimum values of an Array : ")
a = np.array([2,5,8,1,99,23,12,14,2,21,45])
print("Maximum element in array :", np.max(a))
print("Location of maximum element in array :", np.argmax(a))
print("Minimum element in array :", np.min(a))
print("Location of Minimum element in array :", np.argmin(a))

input("Press Enter key to exit ")