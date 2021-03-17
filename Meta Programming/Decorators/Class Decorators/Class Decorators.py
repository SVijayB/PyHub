# Under Meta Programming there are three types :
# 1) Decorators, 2) Class Decorators and 3) Meta Classes
# However, Class Decorators are also a part of Decorators.
# Example :
class x:
    def __init__(self):
        print("An instance or object was initialised")

    # if you mention *args, you can pass any number of arguments
    # kwargs means that you can recieve arguments as or in the form of a dictionary.
    def __call__(self, *args, **kwargs):
        print("Arguments are ", args, kwargs)


a = x()
print("Calling objects or arguments")
a(4, 5, z=12, v=20)
print("Calling call function again")
a(8, 9, r=30, t=40, z="hey")  # Using a class as a repeatable code
