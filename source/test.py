def match(pattern, text):
    i = 0
    match = ""
    sign = ""
    after_sign = ""
    index = ""
    if len(pattern) == 0 and len(text) == 0:
        return True
    if len(pattern) > 0 and pattern[0] == "*" and len(text) == 0:
        return True
    while i < len(pattern)-1:
        if pattern[i].isalpha():
            continue
        else:
            sign = pattern[i]
            index = i
            after_sign = pattern[(i+1-len(pattern)):]
        i+=1
    if sign == "*":
        for i in range(index):
            if pattern[index-1] == text[index-1] and after_sign in text:
                return True
            else:
                return False
    if sign == "?":
        for i in range(index):
            if pattern[index-1] == text[index+1]:
                return True
            else:
                return False
