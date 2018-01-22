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
print(make_anagram("tacohole"))

# recursive method to convert list of str into different lists containing the str element
def permutation(text):
    list = list(text)
    if len(list) == 0:
        return []
    if len(list) == 1:
        return [list]
    result = []
    # calculate the permutation
    for i in range(len(list)):
        item = list[i]
        # extract out the rest of the list except for item
        remain = list[:i] + list[i+1:]
        for j in permutation(remain):
            # generate list that starts with each different element of str list
            result.append([item] + j)
    return result



