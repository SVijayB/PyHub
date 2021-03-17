# Unary operator overloading using magic methods.
def doc():
    """
    Types of Unary operators :
    opr         Magic                     Job
    -         __neg__(self,others)        Neg
    +         __pos__(self,others)        Pos
    abs       __abs__(self,others)        Abs
    ~         __invert__(self,others)     Invert
    cmp       __complex__(self,others)    Complex
    int       __int__(self,others)        Integer
    long      __long__(self,others)       Long
    float     __float__(self,others)      Float
    oct       __oct__(self,others)        Octal
    hex       __hex__(self,others)        Hexa
    """


print(doc.__doc__)
print("EXAMPLE : ")


class x:
    def __init__(self, y):
        self.y = y

    def __neg__(self):
        return self.y

    def __pos__(self):
        return self.y

    def __invert__(self):
        return self.y


if __name__ == "__main__":
    obj = x(-2 * 2)
    print(-obj)
    print(+obj)
    print(~obj)
