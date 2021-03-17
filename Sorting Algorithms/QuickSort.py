def partition(lst, strt, end):
    pindex = strt
    for i in range(strt, end - 1):
        if lst[i] <= lst[end - 1]:
            lst[pindex], lst[i] = lst[i], lst[pindex]
            pindex += 1
    lst[pindex], lst[end - 1] = lst[end - 1], lst[pindex]
    return pindex


def quickSort(lst, strt=0, end=0):
    if strt >= end:
        return
    pivot = partition(lst, strt, end)
    quickSort(lst, strt, pivot)
    quickSort(lst, pivot + 1, end)


lst = list(map(int, input("Enter the number list: ").split()))
quickSort(lst, end=len(lst))
print(lst)
