def palindrom_permu(text):
    str_len = len(text)
    list_str = text.split(" ")
    mid = 0
    # 1. if len of str is even
    if str_len % 2 == 0:
        mid = 0
    else:
        mid = len(str_len) // 2 + 1
    # 2. make histogram of palindrom permutations
    for i in range(1, list_str):

    # 3. consider two cases : 1. even num, 2: odd num
