# function to print the minimum of array.

import sys


def min_of_array(arr, min_so_far=sys.maxsize):
    if len(arr) == 0:
        print(min_so_far)
        return
    new_min = min(min_so_far, arr[0])
    min_of_array(arr[1:], new_min)


arr = list(map(int, input().split()))
min_of_array(arr)
