def doc():
    """
    Class methods are the third and final OOP method type to know. Class methods know about their class.
    They can’t access specific instance data, but they can call other static methods.
    Class methods don’t need self as an argument, but they do need a parameter called cls.
    This stands for class, and like self, gets automatically passed in by Python.

    Class methods are created using the @classmethod decorator.
    """


print(doc.__doc__)
print("Example : ")


class temp:
    def __init__(self):
        print("Constructor Function")  # Function is called in class method.

    @classmethod  # Used to tell Python that the method is a class method
    def class_method(cls):  # cls is used instead of self in class method
        print("Class method")
        cls.static_method(
            "1StranGe"
        )  # Class methods can access static methods in the same class.

    @staticmethod  # Used to tell Python that the method is a static method.
    def static_method(name):  # Don't have to use self for static methods.
        print("Static Method")
        print("Hey! This is", name)


obj = temp()
obj.class_method()  # Object is needed for Class method
print("\nView code and read comments for better understanding.")
