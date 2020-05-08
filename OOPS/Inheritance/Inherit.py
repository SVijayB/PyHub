class parent:
    def _init_(self):
        print("Calling Parent Constructor")
    
    def parentmethod(self):
        print("Calling Parent Method")

    def parentmethod2(self):
        print("Calling the second parent method")

class child(parent):
    def _init_(self):
        print("Calling Child Constructor")

    def childmethod(self):
        print("Calling the Child Method")

    def parentmethod2(self):
        print("Modified parent method 2")

p = parent()
c = child()

p.parentmethod()        # Accessing Parent Method
c.childmethod()         # Accessing Child Method
c.parentmethod()        # Accessing the inherited parent method from child class.  
p.parentmethod2()       # Accessing the 2nd parent method from parent class
c.parentmethod2()       # Accessing the 2nd parent method from the child class after modification

print("\nView code and read comments for better understanding.")

# Parent class cannot access child class. However, the child class can access the parent class.
