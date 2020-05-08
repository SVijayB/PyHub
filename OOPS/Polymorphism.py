def doc():
    """
Polymorphism allows methods that perform similar or closely related functions to be accessed
through a common name. For example, a program performs operations on an array of numbers which can be
int, float or double type.
    """
print(doc.__doc__)
print("Example : ")
class cat:
    def name(self):
        print("Cat")
    def sound(self):
        print("Meow meow")
    def colour(self):
        print("Cats come in various colours.")
class dog:
    def name(self):
        print("Dog")
    def sound(self):                # Same function name.
        print("Woof woof")
    def colour(self):               # Same function name.
        print("Dogs come in various colours.")

def animal_properties(animal):
    animal.name()
    animal.sound()
    animal.colour()

animal_properties(cat())
animal_properties(dog())

print("If you noticed that in the above example, function names remain same and yet they have differnt definations")