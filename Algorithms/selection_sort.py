
import sys
A = [64, 25, 12, 22, 11]


for i in range(len(A)):
	
	
	for j in range(i+1, len(A)):
		if A[min_idx] > A[j]:
			min_idx = j
			
	# Swap the found minimum element with
	# the first element	
	A[i], A[min_idx] = A[min_idx], A[i]


print ("Sorted array")
for i in range(len(A)):
	print("%d" %A[i],end=" ")
