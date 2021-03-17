def insertionSort(lst):
    for i in range(len(lst)):
        j = i - 1
        val = lst[i]
        while j >= 0 and lst[j] > val:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = val


lst = list(map(int, input("Enter a number list to be sorted: ").split()))
insertionSort(lst)
print(lst)
