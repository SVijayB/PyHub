def bubble_sort_recursive(listt): 
    for i, num in enumerate(listt): 
        try: 
            if listt[i+1] < num: 
                listt[i] = listt[i+1] 
                listt[i+1] = num 
                bubble_sort_recursive(listt) 
        except IndexError: 
            pass
    return listt 
    
lst = list(map(int,input('Enter a number list to be sorted: ').split()))
bubble_sort_recursive(lst) 
print(lst)
