# Comparison operators overloaded using python's magic methods.
def doc():
    """
    Types of comparison operators :
    opr         Magic
    <       Obj.__lt__(self,others)
    >       Obj.__gt__(self,others)
    ==      Obj.__eq__(self,others)
    >=      Obj.__ge__(self,others)
    <=      Obj.__le__(self,others)
    !=      Obj.__ne__(self,others)
    """


print(doc.__doc__)
print("EXAMPLE : ")


class comparison:
    def __init__(self, x):
        self.x = x

    def __lt__(self, other):
        return self.x < other.x

    def __gt__(self, other):
        return self.x > other.x

    def __eq__(self, other):
        return self.x == other.x


if __name__ == "__main__":
    a = comparison(2)
    b = comparison(3)
    print(a < b)
    print(a > b)
    print(a == b)
