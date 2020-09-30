def merge(lst1,lst2):
    lst = []
    while lst1 and lst2:
        if lst1[0] < lst2[0]:
            lst.append(lst1[0])
            lst1.remove(lst1[0])
        elif lst1[0] > lst2[0]:
            lst.append(lst2[0])
            lst2.remove(lst2[0])
        else:
            lst.append(lst1[0])
            lst1.remove(lst1[0])
            lst2.remove(lst2[0])
    if lst1:
        lst.extend(lst1)
    elif lst2:
        lst.extend(lst2)
    return lst

def mergeSort(lst):
    if len(lst) <= 1:
        return lst
    mid = int(len(lst)/2)
    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])
    return merge(left,right)

lst = list(map(int,raw_input('Enter the number list: ').split()))
print(mergeSort(lst))