import time
import re
import random

def autocomplete(prefix, word_list):
    # call binarysearchRecursive and findPrefixWord
    index = binarySearch(word_list, prefix)
    findPrefixWord(index, prefix, word_list)

# binary search iteratively to find words mathes with prefix
def findPrefixWord(mid_index, prefix, word_list):
    found_words = []
    left_index = mid_index - 1
    right_index= mid_index + 1
    if prefix == "":
        return complete_words
    if word_list[mid_index].startswith(prefix):
        found_words.append(word_list[mid_index])
    # if left or right matches with prefix, move toward middle
    while left_index < right_index:
        if word_list[left_index].startswith(prefix):
            left_index += 1
            found_words.append(word_list[left_index])
        if word_list[right_index].startswith(prefix):
            right_index -= 1
            found_words.append(word_list[right_index])
        return found_words

# find index of the word that matches with prefix
def binarySearch(word_list, prefix, left_index, right_index):
    if left_index == None and right_index == None:
        left_index = 0
        right_index = len(word_list) - 1

    mid_index = left_index + (right_index - left_index) / 2
    mid = word_list[mid_index]
    prefix_len = len(prefix)

    if left_index > right_index:
        return right_index
    # if prefix is equal to the first part (till the end of prefix) of the middle item, return index of middle item
    if mid[:mid_index] == prefix:
        return mid_index
    elif mid[:prefix_len] < prefix:
        mid_index += 1
        left_index = mid_index
        return binarySearch(word_list, prefix, left_index, right_index)
    elif mid[:prefix_len] > prefix:
        mid_index -= 1
        right_index = mid_index
        return binarySearch(word_list, prefix, left_index, right_index)


def benchMark(prefix, word_list):
    start = time.time()
    autocomplete(prefix, word_list)
    end = time.time()
    benchMark = end - start
    return benchMark

def get_words(file):
    with open(file, 'r') as f:
        word_list = f.read().lower().split()
        word_list.sort()
    return word_list

if __name__ == '__main__':
    word_list = get_words('/usr/share/dict/words')
    prefix = "appl"
    time = benchMark(prefix, word_list)
    print(time)
