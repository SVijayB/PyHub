"""implementation of central limit theorem"""

import math

x = int(input())
n = int(input())
mean = float(input())
sigma = float(input())


Xmean = mean * n
Smean = math.sqrt(n) * sigma

Z = (x - Xmean) / (Smean * math.sqrt(2))
res = 0.5 * (1 + math.erf(Z))

print(round(res, 4))
