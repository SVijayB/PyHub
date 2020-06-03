# A python generator is a simple way of using iterables.
# Let us see string reversal using generators.

def reverse(string):
    length = len(string)
    for i in range (length -1, -1, -1): # The three -1 automatically reverses the string
        yield string[i]
    
for char in reverse("Vijay"):
    print(char)