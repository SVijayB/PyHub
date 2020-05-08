# Accessing Class Attributes.
class temp:
    x = "Hello World!"
    print(x)

print("\nAccessing variable outside the class:")
a = temp()
print(a.x)

class temp:
    def sum(self):
        a = 5
        b = 5
        print(a+b)

print("\nAccessing function present in class:")
a = temp()
a.sum()