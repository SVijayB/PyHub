
# program to sort a list by using bubble sort
def bubbleSort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]

lst = list(map(int,input('Enter a number list to be sorted: ').split()))
bubbleSort(lst)
print(lst)
