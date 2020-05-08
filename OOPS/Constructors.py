class temp:
    def __init__(self):
        i = 5
        print("The object has been successfully created")

a = temp()

class temp:
    def __init__(self,object):
        i = 5
        x = "Hello World!"
        print(object)

a = temp("Object has been successfully created!")
print()

class temp:
    def __init__(self):
        self.i = 0
    def number(self,i):
        self.i = i
        print("Number :", i)
a = temp()
a.number(5)

def constructors():
    """
    A constructor is a special kind of method that python calls when it instantiates an object using 
    the definations found in your class. Python relies on the constructor to perform tasks such as 
    initializing(assigning values to) any instance variables that the object will need when it starts.
    Constructors can also verify that there are enough resources for the object and perform any other 
    start-up task you can think of.

    Every class always has a constructor. When you create a class without a constructor, it automatically
    creates a deafult constructor that does nothing.
    """
print(constructors.__doc__)