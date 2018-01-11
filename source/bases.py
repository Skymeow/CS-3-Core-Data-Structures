#!python
from functools import reduce
import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    exp = len(digits) - 1
    base_ten = 0
    # ord(97) is 'a', ord(123) is 'z'
    for i in digits:
        # if i is letter
        if ord(i) >= 97 and ord(i) <= 123:
            # convert letter into base 10
            i = ord(i) - 97
        else:
            i = int(i)
        base_ten += i * pow(base, exp)
        exp -= 1
    return base_ten
# def encode(number, base):
#     """Encode given number in base 10 to digits in given base."""
#     encode_list = decode_dict = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
#     assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
#     # Handle unsigned numbers only for now
#     assert number >= 0, 'number is negative: {}'.format(number)
#     # TODO: Encode number in binary (base 2)
#     bit_list = []
#     if number == 0:
#         return [0]
#     # while number is non zero
#     while number:
#         bit = number % base
#         bit = encode_list[bit]
#         bit_list.append(bit)
#         number = number >> 1
#     str_result = reduce(lambda x, y: x+y, bit_list[::-1])
#     int_result = str_result
#     return int_result

def encode(number, base):
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    assert number >= 0, 'number is negative: {}'.format(number)
    n = 0
    current = 0
    bit_list = []
    # find the biggest exponential of base within number
    while pow(base, n) <= number/base:
        n+=1
   # find how many times the number has to the biggest exponential
    while n >= 0:
        if pow(base, n) <= number:
            current += 1
            number -= pow(base, n)
        else:
            if current >= 10:
                # char(87) is 'a', so we convert it into tr
                current = chr(current + 87)
            bit_list.append(current)
            # if current is 0, then append nothing to bit_list
            if current == "0":
                bit_list.append("")
            # reset current into 0 and begin next iteration
            current = 0
            n -= 1
    return "".join(str(e) for e in bit_list)

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)

    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    print(decode('1010', 4), 68)
    print(decode("c9", 16))
    # print(decode("1101", 2))
    # print(decode('1010', 2))
    # print(encode(13, 2), "1101")
    # print(encode(248975, 4), '330302033')
    # print(encode(64, 10), "64") #'64'
    # print(encode(255, 16), 'ff') #'ff'
    # print(encode(1234, 2), '10011010010') #'10011010010'
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
