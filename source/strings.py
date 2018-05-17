#!python
# this function is for test if all letters in patter matches text regarless of order
# def contains(text, pattern):
#     """Return a boolean indicating whether pattern occurs in text."""
#     assert isinstance(text, str), 'text is not a string: {}'.format(text)
#     assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
#     i = 0
#     end = len(text) - 1
#     pattern_index = 0
#     check = 0
#     while i <= end:
#         # if first item found, check +1
#         if pattern[pattern_index] == text[i]:
#             check += 1
#         else:
#             check -= 1

#         if check < pattern_index:
#             return False
#         else:
#             pattern_index += 1

#         if pattern_index == len(pattern) - 1:
#             return True
#         i += 1

# strings are immutable in every language so slice is copying, so run time depends on the lens of slice to copy
# wrost case: O(n*p)
#def contains(text, pattern):
#    """Return a boolean indicating whether pattern occurs in text."""
#    assert isinstance(text, str), 'text is not a string: {}'.format(text)
#    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
#    if pattern == '':
#        return True
#    text_end = len(text)
#    pattern_end = len(pattern)
#    for text_index in range(0, text_end):
#        if text[text_index] == pattern[0]:
#            for pattern_index in range(0, pattern_end):
#                if pattern_index + text_index > text_end - 1 or not text[text_index+pattern_index] == pattern[pattern_index]:
#                    print(text_index, pattern_index)
#                    break
#                elif pattern_index == pattern_end - 1 and text[text_index+pattern_index] == pattern[pattern_index]:
#                    return True
#    return False
#
#def find_index(text, pattern):
#    """Return the starting index of the first occurrence of pattern in text,
#    or None if not found."""
#    # annotate run time
#    assert isinstance(text, str), 'text is not a string: {}'.format(text)
#    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
#    if pattern == '':
#        return 0
#    i = 0
#    end = len(text)
#    while i < end:
#        # if first item found, check +1
#        if pattern[0] == text[i]:
#            for n in range(0, len(pattern)):
#                # if the pattern character doesn't match character in text, or index out of text range
#                if text[i+n] != pattern[n]:
#                    break
#                if i+n > len(text) - 1:
#                    # exit out of for loop
#                    break
#                # ran through all character in pattern and all matched
#                elif n == len(pattern) - 1 and text[i+n] == pattern[n]:
#                    return i
#        i += 1
#    return None
#
#
#
#def find_all_indexes(text, pattern):
#    """Return a list of starting indexes of all occurrences of pattern in text,
#    or an empty list if not found."""
#    assert isinstance(text, str), 'text is not a string: {}'.format(text)
#    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
#    if pattern == '':
#        return [i for i in text]
#    i = 0
#    list_index = []
#    end = len(text)
#    while i < end:
#        # if first item found, check +1
#        if pattern[0] == text[i]:
#            for n in range(0, len(pattern)):
#                # if the pattern character doesn't match character in text, or index out of text range
#                if text[i+n] != pattern[n] or i+n > len(text) - 1:
#                    break
#                # ran through all character in pattern and all matched
#                elif n == len(pattern) - 1 and text[i+n] == pattern[n]:
#                    list_index.append(i)
#        i += 1
#    return list_index
#
#
#
#def test_string_algorithms(text, pattern):
#    found = contains(text, pattern)
#    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
#    # TODO: Uncomment these lines after you implement find_index
#    index = find_index(text, pattern)
#    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
#    # TODO: Uncomment these lines after you implement find_all_indexes
#    indexes = find_all_indexes(text, pattern)
#    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))
#
#
#def main():
#    """Read command-line arguments and test string searching algorithms."""
#    import sys
#    args = sys.argv[1:]  # Ignore script file name
#    if len(args) == 2:
#        text = args[0]
#        pattern = args[1]
#        test_string_algorithms(text, pattern)
#    else:
#        script = sys.argv[0]
#        # print('Usage: {} text pattern'.format(script))
#        # print('Searches for occurrences of pattern in text')
#        # print("\nExample: {} 'abra cadabra' 'abra'".format(script))
#        print(contains('aaaaaab', 'aaab'))
#        # print("find_index('abra cadabra', 'abra') => 0")
#        # print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")
#
#
#if __name__ == '__main__':
#    main()

def count_substring(string, sub_string):
    count = 0
#    i = 0
    length_sub = len(sub_string)
    
    for i in range(len(string)):
        if string[i] == sub_string[0]:
            for j in range(1, length_sub):
                if i+j > len(string) - 1:
                    break
                if string[i+j] == sub_string[j]:
                    if j == length_sub - 1:
                        count += 1
                else:
                    break
        print(count)


#    while i < len(string):
#        if string[i] == sub_string[0]:
#            j = 1
#            while j < len(sub_string) and i < len(sub_string):
#                if string[i+1] == sub_string[j]: #D, D
#                    j += 1
#                    i += 1
#                    print(i,j)
#                else:
#                    break
#            if j == len(sub_string) - 1:
#                count += 1
#                i += 1
#                print("i", i)
#                print("hey matched")
#        else:
#            i += 1

#    for index, char in enumerate(string):
#        if char == sub_string[0]:
#            chunk = string[index : index + length]
#            if chunk == sub_string:
#                count += 1


count_substring("ABCDCDCDCABCDC", "CDC")
