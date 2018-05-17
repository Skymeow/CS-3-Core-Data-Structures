import time
import re
import random

def autocomplete(prefix, word_list):
    # first to find the index of the word that's most similar to prefix
    index = binarySearch(word_list, prefix)
    # print("main index", index)
    # then set the word to be middle and go search left and right to find all the word matches with prefix
    findPrefixWord(index, prefix, word_list)

# binary search iteratively to find words mathes with prefix
def findPrefixWord(mid_index, prefix, word_list):
    found_words = [word_list[mid_index]]
    # print(mid_index)
    left_index = mid_index - 1
    right_index= mid_index + 1
    if prefix == "":
        return found_words

    # if left or right matches with prefix, move toward middle
    while word_list[left_index].startswith(prefix) or word_list[right_index].startswith(prefix):
        if word_list[left_index].startswith(prefix):
            found_words.append(word_list[left_index])
            left_index -= 1
        if word_list[right_index].startswith(prefix):
            found_words.append(word_list[right_index])
            right_index += 1
    return found_words

# find index of the word that matches with prefix
def binarySearch(word_list, prefix, left_index=None, right_index=None):
    if left_index is None and right_index is None:
        left_index = 0
        right_index = len(word_list) - 1

    mid_index = int(left_index + (right_index - left_index) / 2)
    # print("mid_index", mid_index)
    mid = word_list[mid_index]
    prefix_len = len(prefix)

    # if prefix is equal to the first part (till the end of prefix) of the middle item, return index of middle item

    if mid[:prefix_len] == prefix:
        # print(mid_index)
        return mid_index
    if left_index > right_index:
        # print("right_index", right_index)
        return right_index

    if mid[:prefix_len] < prefix:
        mid_index += 1
        left_index = mid_index
        return binarySearch(word_list, prefix, left_index, right_index)
    if mid[:prefix_len] > prefix:
        mid_index -= 1
        right_index = mid_index
        return binarySearch(word_list, prefix, left_index, right_index)


def benchMark(prefix, word_list):
    start = time.time()
    result = autocomplete(prefix, word_list)
    print("result", result)
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
    # binarySearch(word_list, prefix)
