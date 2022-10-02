import time

def sumOfDiv(x):
	sum = 1
	for i in range(2, x):
		if x % i == 0:
			sum += i
	return sum

def isAmicable(a, b):
	if sumOfDiv(a) == b and sumOfDiv(b) == a:
		return True
	else:
		return False

def countPairs(a, n):
	Pairs = []
	for i in range(a, n):
		for j in range(i + 1, n):
			if isAmicable(i, j):
				Pairs.append((i,j))
	return Pairs

a = list(map(int,input("Enter the range in a single line: ").split(" ")))
print("\nThe amicable pairs are: ")
res = countPairs(a[0],a[1])
for i in res:
    print(i)
print()
