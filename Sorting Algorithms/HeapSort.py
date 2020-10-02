
class MaxHeap:
    def __init__(s):
        s.lst = [0]
    
    def insert(s,val):
        s.lst[0] += 1
        s.lst.append(val)
        ind = s.lst.index(val)
        while ind > 1:
            if s.lst[int(ind/2)] < s.lst[ind]:
                s.lst[int(ind/2)],s.lst[ind] = s.lst[ind],s.lst[int(ind/2)]
            ind = int(ind/2)

    def delete(s):
        retval = s.lst[1]
        s.lst[1] = s.lst[s.lst[0]]
        s.lst[0] -= 1
        i = 1
        while  i*2 <= s.lst[0] and i*2+1 <= s.lst[0]:
            if s.lst[i*2] > s.lst[i] and s.lst[i*2] > s.lst[i*2+1]:
                s.lst[i*2],s.lst[i] = s.lst[i],s.lst[i*2]
                i = i*2
            elif s.lst[i*2+1] > s.lst[i]:
                s.lst[i*2+1],s.lst[i] = s.lst[i],s.lst[i*2+1]
                i = i*2+1
            else:
                break
        if i*2 <= s.lst[0] and s.lst[i*2] > s.lst[i]:
            s.lst[i*2],s.lst[i] = s.lst[i],s.lst[i*2]
        return retval

    def heapSort(s):
        l = []
        while s.lst[0] != 0:
            l.append(s.delete())
        s.lst[0] = len(l)
        s.lst[1:] = l[::-1] 

    def print_heap(s):
        print(s.lst[1:s.lst[0]+1])

heap = MaxHeap()

lst = list(map(int,input('Enter the list of numbers to be sorted: ').split()))

for i in lst:
    heap.insert(i)
    heap.print_heap()
heap.heapSort()
heap.print_heap()