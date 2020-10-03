def bubble_sort_recursive(list1): 
    for i, num in enumerate(list1): 
        try: 
            if list1[i+1] < num: 
                list1[i] = list1[i+1] 
                list1[i+1] = num 
                bubble_sort_recursive(list1) 
        except IndexError: 
            pass
    return list1 
    
lst = list(map(int,input('Enter a number list to be sorted: ').split()))
bubble_sort_recursive(lst) 
print(lst)
