print("\nMulti-Level Inheritance :",
"If a class is derived from a derived class, then it's called Multi-level inheritance.",
"\nThat is if you inherit a class that is already a child class for some other parent class,", 
"then it is Multi-Level inheritance")
print("Example : ")
class parent:
    def ParentMethod(self):
        print("Parent method") 

class child(parent):                # Inherited parent class.  
    def ChildMethod(self):
        print("Child method")

class grandchild(child):            # Inherited child class which already inherited parent calss.
    def GrandchildMethod(self):
        print("GrandChild Method")

p = parent()
c = child()
g = grandchild()

p.ParentMethod()                    # Calling parent method
c.ChildMethod()                     # Calling child method
g.GrandchildMethod()                # Calling GrandChild method
print()
g.ParentMethod()                    # Calling parent method using the Grandchild Object
g.ChildMethod()                     # Calling the Child method using the Grandchild Object
g.GrandchildMethod()                # Calling the GrandchildMethod using the Grandchild Object

print("\nIn this example, the child class inherited the parent class and the grandchild class inherited",
"\nthe child class. Therefore the grandchild class inherited both parent and child class.")
print("\nView code and read comments for better understanding.")