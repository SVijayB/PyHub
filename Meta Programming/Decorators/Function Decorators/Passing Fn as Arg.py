# Pass a function as an argumenet to another function.
def x(func):
    print("Hey I am the function that has a function as argument!")


def y():
    print("Hey! I am the function being passed as an argument to another function")


x(y())  # Argument function is executed first and then the calling function.

input("Press Enter key to exit ")
