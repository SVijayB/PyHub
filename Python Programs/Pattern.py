n=int(input())
length=n*2-1
for i in range(legth):
	for j in range(legth):
		t=min(i,j)
		t=min(t,legth-i-1)
		t=min(t,legth-j-1)
		print(n-t)
