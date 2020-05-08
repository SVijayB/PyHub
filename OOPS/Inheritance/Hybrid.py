print("\nHybrid Inheritance is a combination of both Multi-level and Multiple(Hierarchial) Inheritance")

class parent:
    def ParentMethod(self):
        print("Parent Method") 

class child(parent):                # Multiple Inheritance  
    def ChildMethod(self):
        print("Child Method")

class child2(parent):               # Multiple Inheritance
    def child2method(self):
        print("Child2 Method")

class GrandChild(child,child2):     # Multi-Level Inheritance
    def GrandChildMethod(self):
        print("GrandChild Method")

p = parent()
c = child()
c2 = child2()
g = GrandChild()

g.ParentMethod()                    # Calling parent method using the Grandchild Object
g.ChildMethod()                     # Calling the Child method using the Grandchild Object
g.GrandChildMethod()                # Calling GrandChild method using the Grandchild Object.
g.child2method()                    # calling child2 method using the Grandchild Object.

print("This is Hybrid Inheritance as it has multiple and multi-level inheritance.")
print("\nView code and read comments for better understanding.")
