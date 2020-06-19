# The instance of a class is called a meta class.
# A metaclass is a class whose instances are classes.
def metafunction():
    print("This is the metaclass function")

class inherit():
    def func(self):
        print("This is the inherited method")
    
metaobject = type('meta', (inherit, ),dict(name = "Vijay", metafunction=metafunction))
print(type(metaobject))
b = metaobject()
print(type(b))

b.func()
print(b.name)