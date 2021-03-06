from random import randint
import Settings
from Settings import swap

def randomize_select(array: list, left: int, right: int):
    i = randint(left, right)
    swap(array, i, right)
    #array[i], array[right] = array[right], array[i]
    return partition(array, left, right)


def partition(array: list, left: int, right: int):
    pivot = array[right]
    i = left - 1
    for j in range(left, right):
        Settings.quick_comparisons += 1
        if array[j] <= pivot:
            i += 1
            swap(array, i, j)
    i += 1
    swap(array, i, right)
    return i  
            

def quick_sort(array: list, start: int, end: int):
    if start < end:
        q = randomize_select(array, start, end)
        quick_sort(array, start, q -1)
        quick_sort(array, q + 1, end)


def k_smallest(array: list, left: int, right: int, k: int):
    curr = randomize_select(array, left, right)
    if curr == k: 
        return curr
    if curr > k :
        return k_smallest(array, left, curr - 1, k)
    return k_smallest(array, curr + 1, right, k)


def k_smallest_list(array: list, left: int, right: int, k: int):
    curr = randomize_select(array, left, right)
    
    if curr == k :
        return curr
    if curr > k :
        return k_smallest(array, left, curr - 1, k)
    return k_smallest(array, curr + 1, right, k)