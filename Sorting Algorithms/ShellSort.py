def shellSort(arr): 
	n = len(arr) 
	gap = n//2

	while gap > 0: 
		for i in range(gap,n): 
			temp = arr[i] 
			j = i 
			while j >= gap and arr[j-gap] >temp: 
				arr[j] = arr[j-gap] 
				j -= gap 
			arr[j] = temp 
		gap //= 2

lst = list(map(int,input('Enter a number list to be sorted: ').split()))
shellSort(lst)
print(lst)
