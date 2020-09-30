def selectionSort(lst):
    for i in range(len(lst)):
        ind = lst.index(min(lst[i:]))
        print(i,ind,min(lst[i:]))
        lst[i],lst[ind] = lst[ind],lst[i]
    return lst

lst = list(map(int,input('Enter the number list: ').split()))
print(lst.index(min(lst)))
print(selectionSort(lst))
