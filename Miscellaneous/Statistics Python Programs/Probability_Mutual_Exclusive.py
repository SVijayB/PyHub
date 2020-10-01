"""
Task
There are urns labeled , , and .

    Urn contains red balls and black balls.
    Urn contains red balls and black balls.
    Urn contains red balls and black balls.

One ball is drawn from each of the urns. What is the probability that, of the balls drawn, are red and is black?
10 / 63
2 / 7
17 / 42
31 / 126

Ans: 17/42
"""

#Code:
from fractions import Fraction

x=[4,3]
y=[5,4]
z=[4,4]

xr=x[0]/sum(x)
yr=y[0]/sum(y)
zr=z[0]/sum(z)

pr=(xr*yr*(zr-1))+(xr*(yr-1)*zr)+((xr-1)*yr*zr)
print(Fraction(pr).limit_denominator())
