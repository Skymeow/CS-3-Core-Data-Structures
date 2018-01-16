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
