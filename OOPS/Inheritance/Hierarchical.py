print(
    "\nIn Hierarchial Inheritance, the parent class can be accessed by several Child classes."
)


class parent:
    def parentmethod(self):
        print("Calling Parent Method")

    def parentmethod2(self):
        print("Calling the second parent method")


class child(parent):
    def childmethod(self):
        print("Calling the Child Method")

    def parentmethod2(self):
        print("Modified parent method 2")


class child2(parent):  # The parent class can be accessed by several other child class
    def child2method(self):
        print("Calling the second child's method")


p = parent()
c = child()
c2 = child2()

p.parentmethod()  # Accessing Parent Method
c.childmethod()  # Accessing Child Method
c.parentmethod()  # Accessing the inherited parent method from child class.
p.parentmethod2()  # Accessing the 2nd parent method from parent class
c.parentmethod2()  # Accessing the 2nd parent method from the child class after modification
c2.child2method()  # Accessing the 2nd child's method
c2.parentmethod()  # Accessing the parent class from the 2nd child class.

print("\nView code and read comments for better understanding.")

# Parent class cannot access child class. However, the child class can access the parent class.
