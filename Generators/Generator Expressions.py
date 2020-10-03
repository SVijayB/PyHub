# You can create a generator using a generator expression like a lambda function.
# This function does not need or use a yield keyword.
# Syntax : Y = ([ Expression ])

y = [1,2,3,4,5]

print([x**2 for x in y])

print("\nDoing this without using the generator expressions :")
length = len(y)
print((x**2 for x in y).__next__())
input("Press Enter key to exit ")
