# Binary operator overloading using magic methods.
def doc():
    """
Types of binary operators : 
opr         Magic                   Job
+       __add__(self,others)        Add
-       __sub__(self,others)        Sub
*       __mul__(self,others)        Mul
/       __div__(self,others)        Div
//      __floordiv__(self,others)   Floor
%       __mod__(self,others)        Mod
**      __pow__(self,others)        Power
<<      __lshift__(self,others)     Left Shift
>>      __rshift__(self,others)     Right Shift
$       __and__(self,others)        AND
^       __xor__(self,others)        XOR
|       __or__(self,others)         OR
    """
print(doc.__doc__)
print("EXAMPLE : ")
class operators:
    def __init__(self, *arguments):
        if (len(arguments)==0):
            self.numbers = (0,0)
        else:
            self.numbers = arguments
    
    def __add__(self,other):
        sum = tuple(x + y for x,y in zip(self.numbers, other.numbers))      # Vector Addition
        return operators(*sum)

    def __mul__(self,other):
        mul = tuple(x * y for x,y in zip(self.numbers, other.numbers))      # Vector Multiplication
        return operators(*mul)
    
a = operators(2,3)
b = operators(5,6)
c = a + b       # __add__ is automatically called
d = a * b       # __mul__ is automatically called
print(c.numbers)
print(d.numbers)
