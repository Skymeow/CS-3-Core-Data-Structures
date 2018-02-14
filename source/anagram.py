def make_anagram(text):
    text.replace(' ', '')
    text.lower()
    arr = []
    if len(text) <= 1:
        yield text
    else:
        # except for the first index
        for element in make_anagram(text[1:]):
            for i in range(len(text)):
                arr.append(element[:i] + text[0:1] + element[i:])
        return arr
# print(make_anagram("tacohole"))

# recursive method to convert str_list of str into different str_lists containing the str element
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
for p in permutation("skyrockk"):
    print(p)


