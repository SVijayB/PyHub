"""print pattern

5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5 

"""
n=int(input())
legth=n*2-1
for i in range(legth):
	for j in range(legth):
		t=min(i,j)
		t=min(t,legth-i-1)
		t=min(t,legth-j-1)
		print(n-t,end=" ")
	print()
