# Arithmetic and Assignment Operators : 
x = 5       # Assignment operator
print("X :", x)
x += 5
print("X + 5 =" , x)

"""
Similar Operators : 
	+=
	-=
	/=
	x=
	%=
	**= 		#Multiplies the variable by the number of times, eg : x = 5; x**=3 ans is 125
	//=  		#Floor Divison
	&=			#And operation
	|=   		#Or Operation
	^=
	>>= Right Shift
	<<= Left Shift
"""

y = 10
print("Y :" , y)
print("Is X = Y ?" , (x is y))
y = 5
print("Y :",y)
print("Is X = Y ?" , (x is y))

"""
Similarly,
    Identity Operators : 
	is			#Checks whether both the operands refer to the same object or not.
	is not		#Opposite of is operator.

    Membership Operators : 
	    in			#Returns true if specified value is present in the object, else returns false.
	    Not in		#Opposite of in operator.
"""

if(x==y):
    print("X is equal to Y")

if(x!=y):
    print("X is not equal to Y")

"""
Comprison Operators : 
	==
	!=
	<>
	>
	<
	>=
	<=

Logical Operators : 
	&	#Logical And
	|	#Logical Or
	~	#Logical Not
"""