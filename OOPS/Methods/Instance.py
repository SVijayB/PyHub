def doc():
    """
    Instance methods must have self as a parameter, but you don’t need to pass this in every time.
    Self is another Python special term. Inside any instance method,
    you can use self to access any data or methods that may reside in your class.
    You won’t be able to access them without going through self.

    Finally, as instance methods are the most common, there’s no decorator needed.
    Any method you create will automatically be created as an instance method, unless you tell Python otherwise.
    """


print(doc.__doc__)
print("Example : ")


class instance:
    def __init__(self):
        print("Constructor Function")
        self.name = "1StranGe"
        print("All objects have been successfully initialized")

    def instance_method(self):
        print("Instance Method")
        print("Hey! This is", self.name)


obj = instance()
obj.instance_method()
