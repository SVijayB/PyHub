def countingSort(lst):
    newlst = [0]*(max(lst)-min(lst)+1)
    val = min(lst)
    for i in range(len(lst)):
        lst[i] -= val
    for i in lst:
        newlst[i] += 1
    for i in range(1,len(newlst)):
        newlst[i] += newlst[i-1]
    retlst = [0]*len(lst)
    for i in range(len(lst)-1,-1,-1):
        retlst[newlst[lst[i]]-1] = lst[i]+val
        newlst[lst[i]] -= 1
    return retlst

lst = list(map(int,input().split()))
print(countingSort(lst))

