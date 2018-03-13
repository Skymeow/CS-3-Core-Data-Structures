def make_anagram(text):
    text.replace(' ', '')
    text.lower()
    items = text.split(" ")
    if len(text) <= 1:
        yield text
    else:
        # # except for the first index
        # for element in make_anagram(text[1:]):
        #     for i in range(len(text)):
        #         arr.append(element[:i] + text[0:1] + element[i:])
        # return arr
        shuffled_indexes = []
        while len(shuffled_indexes) < len(items):
            rand_index = random.randint(0, len(items) - 1)
            # put unique rand index within the list into shuffled indexes
            if rand_index not in shuffled_indexes:
                shuffled_indexes.append(rand_index)
        anagam = ''
        for ind in shuffled_indexes:
            anagam += items[ind]
        return anagam
print(make_anagram("tacohole"))

# refactor a  recursive method to convert str_list of str into different str_lists containing the str element
def permutation(text):
    str_list = list(text)
    if len(str_list) == 0:
        return []
    if len(str_list) == 1:
        return [str_list]
    result = []
    # calculate the permutation
    for i in range(len(str_list)):
        item = str_list[i]
        # extract out the rest of the str_list except for item
        remain = str_list[:i] + str_list[i+1:]
        for j in permutation(remain):
            # generate str_list that starts with each different element of str str_list
            result.append([item] + j)
    return result
# for p in permutation("skyrockk"):
#     print(p)

def permutation2(text):
    str_list = list(text)
    if len(str_list) == 0:
        return []
    if len(str_list) == 1:
        return [str_list]
    result = []
    extract_arr = []
    for i in range(len(str_list)):
       item = str_list[i]
       remain = str_list[:i] + str_list[i+1:]
       for j in permutation(remain):
            result.append()


def checkAnagram(text1, text2):
    if len(text1) != len(text2):
        return False
    for i in text1:
        if i not in text2:
            return False
    return True


# print(checkAnagram("taco", "cota"))




