from random import randint
from time import time
def partition(arr, p, q): # Time complexity: O(n)
    pivot = arr[p]
    i = p
    for j in range(p+1, q+1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[p], arr[i] = arr[i], arr[p]
    return i    # the index of the pivot

def partition_randomized(arr, p, q):
    """
    To overcome the problem of O(n^2) as the worst case, we will
    choose a random element from the array as a pivot.
     """
    p_rand = randint(p, q)
    arr[p], arr[p_rand] = arr[p_rand], arr[p]
    pivot = arr[p]
    i = p
    for j in range(p+1, q+1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[p], arr[i] = arr[i], arr[p]
    return i    # the index of the pivot

def quick_sort_3partition(arr): # make 3 partitions
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [j for j in arr[1:] if j < pivot]
    equal = [j for j in arr[1:] if j == pivot]
    greater = [j for j in arr[1:] if j > pivot]
    return quick_sort_3partition(less) + equal + [pivot] + quick_sort_3partition(greater)

num_elems = int(input())
l = list(map(int, input().split()))
assert num_elems == len(l)
print(' '.join(map(str, quick_sort_3partition(l))))


def quick_sort(arr, p, r):  # Time complexity (best case): T(n) = O(nlgn), Space complexity: O(1) we haven't used any additional space
    """
    The worst case is O(n^2). It occurs when the array is already sorted or the chosen pivot
    is the maximum of the minimum number. So, it is obvious that the quick sort
    algorithm depends on the choice of the pivot.
     """
    if p < r:
        q = partition_randomized(arr, p, r)    #                                     O(n)
        quick_sort(arr, p, q-1) # sort all the elements before the pivot. T(n/2)
        quick_sort(arr, q+1, r) # sort all the elements after the pivot.  T(n/2)
    return arr
# print(quick_sort([randint(0, 100) for _ in range(5)], 0, 4))

