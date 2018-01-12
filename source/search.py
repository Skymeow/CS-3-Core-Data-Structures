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
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    left = 0
    right = len(array) - 1
    # if we find the item in first index, don't go into while loop
    if array[0] == item:
        return 0
     # make sure mid bigger then 1
    mid = int(left + (right - left) / 2)
    # make sure index doesn't go out of scope,since we are increasing the value of left, decrease the value of right
    while left <= right:
        # item found
        if array[mid] == item:
            return mid
        # if item is in the left of mid, move right one step back to the left
        elif array[mid] > item:
            mid -= 1
            right = mid
        elif array[mid] < item:
            mid += 1
            left = mid




def binary_search_recursive(array, item, left=None, right=None):
    # set the left to be first index, right to last index only once
    if left is None and right is None:
        left = 0
        right = len(array) - 1
    # if goes out of array scope, end the recursive
    if left > right:
        return None
    # if first item is what we want, return 0
    if array[0] == item:
        return 0
    # set mid of left and right
    mid = int(left + (right - left) / 2)
    # return found item index
    if array[mid] == item:
        return mid
    elif item < array[mid]:
        mid -= 1
        right = mid
        return binary_search_recursive(array, item, left, right)
    elif item > array[mid]:
        mid += 1
        left = mid
        return binary_search_recursive(array, item, left, right)

print(binary_search_recursive(['Alex', 'Brian', 'Julia'], "Julia", left=None, right=None))





