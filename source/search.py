#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    # if item not in array:
    #     raise ValueError('item not in the list')
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    arr_length = len(array)
    if index < arr_length:
        if array[index] == item:
            return index
        else:
            index += 1
            return linear_search_recursive(array, item, index)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    left = 0
    right = len(array) - 1
    if array[0] == item:
        return 0
    mid = int(left + (right - left) / 2)
    while left <= right:
        if array[mid] == item:
            return mid
        elif array[mid] > item:
            mid -= 1
            right = mid
        elif array[mid] < item:
            mid += 1
            left = mid




def binary_search_recursive(array, item, left=None, right=None):
    left = array[0]
    right = array[-1]
    left_index = 0
    right_index = len(array) - 1
    mid = int(left_index + (right_index - left_index) / 2)
    if array[mid] == item:
        return mid
    elif item < array[mid]:
        mid -= 1
        right_index = mid
        return binary_search_recursive(array, item, left_index, right_index)
    elif item > array[mid]:
        mid += 1
        left_index = mid
        return binary_search_recursive(array, item, left_index, right_index)







