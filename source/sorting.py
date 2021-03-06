#!python
from binarytree import BinarySearchTree

# small range insertion sort, large range merge sort, if know all in a roll, copy all of them into one chunk(MAIN: USE DIFFERENT SCALE)
def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if not
    for i in range(0, len(items)-1):
        if items[i] > items[i+1]:
            return False
        return True

# def bubble_sort(items):
#     """Sort given items by swapping adjacent items that are out of order, and
#     repeating until all items are in sorted order.
#     TODO: Running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Repeat until all items are in sorted order
#     # TODO: Swap adjacent items that are out of order
#     # multiple assignment
#     # right first, left hand next, (location, value), 0 memory storage
#     # items[i], items[i2] = items[i2], items[i]
#     # (is_sorted, last_sorted) = (false, len(items))
#     isSorted = False
#     length = len(items) - 1
#     while not isSorted and length > 0:
#         # after finish teh for loop, it's issorted is false
#         isSorted = True
#         for i in range(length):
#             # swap is left item is bigger than right
#             if items[i] > items[i+1]:
#                 isSorted = False
#                 temp = items[i]
#                 items[i] = items[i+1]
#                 items[i+1] = temp
#         length -= 1


# def selection_sort(items):
#     """Sort given items by finding minimum item, swapping it with first
#     unsorted item, and repeating until all items are in sorted order."""
#     # TODO: Repeat until all items are in sorted order
#     for i in range(0, len(items)-1):
#         check = i + 1
#     # set first item to be smallest
#         while check < len(items):
#        # swap if mini bigger than the next element
#             if items[check] < items[i]:
#             # temp to store value of temp for future swap
#                 temp = items[check]
#                 items[check] = items[i]
#                 items[i] = temp
#             # if found mini, increase the first item index by 1
#             check += 1

# def insertion_sort(items):
#     """Sort given items by taking first unsorted item, inserting it in sorted
#     order in front of items, and repeating until all items are in order.
#     TODO: Running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Repeat until all items are in sorted order
#     # TODO: Take first unsorted item
#     # TODO: Insert it in sorted order in front of items
#     # how keep track of first unsorted item index?
#     for i in range(0, len(items)-1):
#         # last_index = 0
#         if items[i] > items[i+1]:
#             insert_item = items.pop(i)
#             last_index = i
#             # iterate through items from last sorted item to far left
#             for j in range(last_index-1):
#                 if items[j] > insert_item:
#                     # insert in front of the item if insert_item smaller then it
#                     items.insert(j, insert_item)

# def split_sort_merge(items):
#     """Sort given items by splitting list into two approximately equal halves,
#     sorting each with an iterative sorting algorithm, and merging results into
#     a list in sorted order.
#     TODO: Running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Split items list into approximately equal halves
#     # TODO: Sort each half using any other sorting algorithm
#     # TODO: Merge sorted halves into one list in sorted order
#     mid = len(items) // 2
#     items1 = items[:mid]
#     items2 = items[mid:]
#     selection_sort(items1)
#     selection_sort(items2)
#     # update new merged list into items
#     # items = self.merge(items1, items2)
#     # DEEP COPY! this can change global var items into this new list(reassign new content to the property of old list)
#     items[:] = merge(items1, items2)

# divide log2N time, cause we divide half and half
# def tree_sort(items):
#     binaryTree = BinarySearchTree(items)
#     items[:] = binaryTree.items_in_order()

# def quick_sort(items):
#     i = 0
#     pivot = items[i]
#     while i < len(items)-1:
#         for j in range(i, len(items)-2):
#             # keep iterate if next items after pivot is smaller than pivot, else, swap
#             if items[j] <= pivot:
#                 # increase store (compare) index
#                 i += 1
#                 # swap if next items after pivot is bigger
#                 items[i], items[j] = items[j], items[i]
#         items[i], items[i-1] = items[i-1], items[i]
#         return items

# is logn time to divide cause we pick the pivot arbitrary, so two divided list can be uneven length
# def quick_sort(items):
#     pivot = items[0]
#     lesser_list = []
#     greater_list = []
#     for i in range(1, len(items)):
#         item = items[index]
#         if item <= pivot:
#             lesser_list.append(item)
#         else:
#             greater_list.append(item)
#         quick_sort(lesser_list)
#         quick_sort(greater_list)
#     items[:] = lesser_list + pivot + greater_list

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    # if either of lists are empty, return the non empty one
    # if not len() or not len(r):
    #     return r or l

    merged_list = []
    l_index, r_index = 0, 0

    # keep going if didn't go through merging all left and right list
    while l_index < len(items1) and r_index < len(items2):
        print(l_index, r_index)
        # append smallest item from l or r to merged list
        if items1[l_index] < items2[r_index]:
            merged_list.append(items1[l_index])
            l_index += 1
            print("first", l_index, r_index)
        else:
            merged_list.append(items2[r_index])
            r_index += 1
            print("second", l_index, r_index)
        # if either left or right list finished iteration, add the rest of another part to merged list
    if l_index != len(items1):
        merged_list.extend(items1[l_index:])
    else:
        print("r_index", r_index)
        merged_list.extend(items2[r_index:])

    return merged_list
print(merge([3, 4, 7], [6, 9]))


# run time: o(logn)
def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    # if only has 0 or 1 item in the list means recursive stack is at bottom
    if len(items) == 1:
        return items
        # define middle point
    mid = len(items) // 2
    # recursively calling the sorting function (merge ordered list into new list)
    left = items[:mid]
    right = items[mid:]
    items1 = merge_sort(left)
    items2 = merge_sort(right)
    # merge left and right by calling merge function we made earlier
    items = merge(items1, items2)
    return items
# print(merge_sort([3, 15, 4, 7, 20, 6, 18, 11, 9, 7]))


# def random_ints(count=20, min=1, max=50):
#     """Return a list of `count` integers sampled uniformly at random from
#     given range [`min`...`max`] with replacement (duplicates are allowed)."""
#     import random
#     return [random.randint(min, max) for _ in range(count)]


# def test_sorting(sort=split_sort_merge, num_items=20, max_value=50):
#     """Test sorting algorithms with a small list of random items."""
#     # Create a list of items randomly sampled from range [1...max_value]
#     items = random_ints(num_items, 1, max_value)
#     print('Initial items: {!r}'.format(items))
#     print('Sorted order?  {!r}'.format(is_sorted(items)))

#     # Change this sort variable to the sorting algorithm you want to test
#     # sort = bubble_sort
#     print('Sorting items with {}(items)'.format(sort.__name__))
#     split_sort_merge(items)
#     print('Sorted items:  {!r}'.format(items))
#     print('Sorted order?  {!r}'.format(is_sorted(items)))


# def main():
#     """Read command-line arguments and test sorting algorithms."""
#     import sys
#     args = sys.argv[1:]  # Ignore script file name

#     if len(args) == 0:
#         script = sys.argv[0]  # Get script file name
#         print('Usage: {} sort num max'.format(script))
#         print('Test sorting algorithm `sort` with a list of `num` integers')
#         print('    randomly sampled from the range [1...`max`] (inclusive)')
#         print('\nExample: {} bubble_sort 10 20'.format(script))
#         print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
#         print('Sorting items with bubble_sort(items)')
#         print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')
#         return

#     # Get sort function by name
#     if len(args) >= 1:
#         sort_name = args[0]
#         # Terrible hack abusing globals
#         if sort_name in globals():
#             sort_function = globals()[sort_name]
#         else:
#             # Don't explode, just warn user and show list of sorting functions
#             print('Sorting function {!r} does not exist'.format(sort_name))
#             print('Available sorting functions:')
#             for name in globals():
#                 if name.find('sort') >= 0:
#                     print('    {}'.format(name))
#             return

#     # Get num_items and max_value, but don't explode if input is not an integer
#     try:
#         num_items = int(args[1]) if len(args) >= 2 else 20
#         max_value = int(args[2]) if len(args) >= 3 else 50
#         # print('Num items: {}, max value: {}'.format(num_items, max_value))
#     except ValueError:
#         print('Integer required for `num` and `max` command-line arguments')
#         return

#     # Test sort function
#     test_sorting(sort_function, num_items, max_value)


# if __name__ == '__main__':
#     main()
