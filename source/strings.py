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

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    i = 0
    text = text.replace(' ', '')
    end = len(text) - 1
    pattern_index = 0
    check = 0
    while i <= end:
        # if first item found, check +1
        if pattern[pattern_index] == text[i]:
            check += 1
            next_i = i
        else:
            check -= 1
            i += 1
        if check < pattern_index:
            return False
        else:
            pattern_index += 1

        # delete matched pattern letter
        text = text[(next_i+1):]
        # print(text, check, pattern_index-1)
        if len(text) <= 0:
            return False

        if pattern_index == len(pattern) - 1:
            return True
        # i += 1


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
