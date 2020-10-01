"""Find out the prosibility of coin change"""

import math
import os
import random
import re
import sys

w=10;
coins=[1,5,6,9]
a=[[0]*(w+1)]*len(coins)
for j in range(w+1):
    a[0][j]=j
for i in range(1,len(coins)):
    a[i][0]=0
    for j in range(1,w+1):
        if coins[i]>j:
            a[i][j]=a[i-1][j]
        else:
            a[i][j]=min(a[i-1][j],1+a[i][j-coins[i]])

print(a[len(coins)-1][w])


