import math

print(
    '\nExample of Operator Overloading is the "+" operator.',
    "It is used to add two numbers and concat two strings.",
)
print("Another Example : ")


class circle:
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def area(self):
        return math.pi * self.radius**2

    def __add__(self, another):
        return circle(self.radius + another.radius)


c1 = circle(5)
print("Radius of first circle :", c1.getRadius())

c2 = circle(7)
print("Radius of second circle :", c2.getRadius())

c3 = c1 + c2
print('Using the "+" Operator to add two objects now :', c3.getRadius())
print(
    "Area of the circle whose radius is the sum of radius of the other two circles :",
    c3.area(),
)
