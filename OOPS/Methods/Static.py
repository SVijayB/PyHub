def doc():
    """
    Static methods are methods that are related to a class in some way,
    but don’t need to access any class-specific data. You don’t have to use self,
    and you don’t even need to instantiate an instance, you can simply call your method.

    The @staticmethod decorator is used to tell Python that this method is a static method.
    """


print(doc.__doc__)
print("Example : ")


class static:
    def __init__(self):
        print(
            "Constructor Function"
        )  # In Static method, the instance is entirely skipped.

    @staticmethod  # Used to tell Python that the method is a static method.
    def static_method(name):  # Don't have to use self for static methods.
        print("Static Method")
        print("Hey! This is", name)


name = static.static_method("1StranGe")  # You don't have to create an object.
print("\nView code and read comments for better understanding.")
