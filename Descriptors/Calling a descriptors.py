# There are two methods :
# Using an instance to call the descriptor and then the instance is used for the owning class.
# Calling a descriptor using another class.
# Most common method is for the descriptor to be invoked automatically when you access an attribute.

# Method 1 : Using an instance to call the descriptor and then using the instance for the owning class.
class cel:
    def __get__(self, instance, owner):
        return 5 * (instance.x - 32) / 9

    def __set__(self, instance, value):
        instance.x = 32 + 9 * value / 5


class temp:
    y = cel()

    def __init__(self, x):
        self.x = x


t = temp(112)
print(t.y)
t.y = 0
print(t.x)

# Method 2 : Calling a descriptor using another class.
class cel:
    def __init__(self, value=0.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class feh:
    def __get__(self, instance, owner):
        return (instance.cel * 9 / 5) + 32

    def __set__(self, instance, value):
        instance.cel = (float(value) - 32) * 5 / 9


class temp:
    cel = cel(112)
    feh = feh()
    print("Celcius Value :", cel.value)


t = temp()
print("After converting to Fahrenheit :", t.feh)

input("Press Enter key to exit ")
