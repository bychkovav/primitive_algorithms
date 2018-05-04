__author__ = 'Alexey'
'''
    sorted_arr is sorted in ascending order
'''
import math
# In case we want to find an item in array
def search_equal(val, sorted_arr):
    start = 0
    end = len(sorted_arr) - 1

    found = False
    while not found:
        index = math.ceil((start + end) / 2)
        if sorted_arr[index] == val:
            return index
        elif sorted_arr[index] > val:
            if end == start:
                break
            end = index
            if index == 1:
                end = 0

        elif sorted_arr[index] < val:
            if end == start:
                break
            start = index

    return None


# In case we want to place the item in array
def search_not_equal(val, sorted_arr):
    start = 0
    end = len(sorted_arr) - 1

    found = False
    while not found:
        index = math.ceil((start + end) / 2)
        if sorted_arr[index] > val:
            if index == 0 or sorted_arr[index - 1] <= val:
                return index
            if index == 1:
                end = 0
            else:
                end = index
        elif sorted_arr[index] < val:
            if index == len(sorted_arr) - 1 or sorted_arr[index + 1] >= val:
                return index
            start = index
        else:
            if index == 0 or index == len(sorted_arr) - 1:
                return index
            return index - 1
