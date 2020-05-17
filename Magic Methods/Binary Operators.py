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