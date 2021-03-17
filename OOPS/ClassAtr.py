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
        print(a + b)


print("\nAccessing function present in class(Method):")
a = temp()
a.sum()


def ClassAtr():
    """
    Difference between Function and Method : Methods are part of a class while functions are not.
    Simply, function and method both look similar as they perform in almost similar way,
    but the key difference is the concept of 'Class and its Object'.
    Functions can be called only by its name, as it is defined independently.
    But methods can’t be called by its name only, we need to invoke the class by a reference of that class
    in which it is defined, i.e. method is defined within a class and hence they are dependent on that class
    """


print(ClassAtr.__doc__)
