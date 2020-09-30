print("Tuples in Python are ordered collection of elements. They are immutable." +
"They can have Strings, numbers, Float, and more or a combination of all of them")
print()

print("For tuples in python, we use round brackets")
a = ("One", 2, "Three", "Four", 5)
print("Tuple a: ", a)
print()

print("Use comma to create a tuple with only one item")
b = ("Only",)
print("Tuple b: ", b)
print()

print("Each element has an unique index starting from 0, similar to a list.")
print("First element in a: ", a[0])
print()

print("Return value of a new tuple can be specified by a range.")
print("Index 2 to 5 in a: ", a[2:4])
print()

print("To change values in a tuple, convert the tuple into a list and make some changes.")
c = ("red", "orange", "blue")
d = list(c)
d[1] = "yellow"
c = tuple(d)
print("Change second element in c: ", c)
print()

print("To delete tuple, use del.")
e = (2, 4, 6)
del e
print()

print("To join tuples, use + operator")
f = ("plus", "minus")
g = (10, 100)
h = f + g
print("Joined tuple is: ", h)
print()

print("Tuple c is: ", c)
print("Length of tuple c: ", len(c))
print()

input("Press any key to exit ")