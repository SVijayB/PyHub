def doc():
    """
    The magic methods in python are like normal methods but with double underscore before and after the method name.
    These double underscores are called dunder. These methods are called dunder or magic methods.
    A constructor function like init is also a magic method.
    Example :
    """


print(doc.__doc__)


class x:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b


obj = x(3, 4)
print("Sum is =", obj.sum())
