__author__ = 'dick'
__email__ = 'ralbayaty@gmail.com'


def reverse(string_val):
    if len(string_val) <= 1:
        return string_val
    return reverse(string_val[1:]) + string_val[0]


def reverse_string(string_val):
    # The input string is assuredly alphanumeric (numbers and letters)
    split_up = []
    split_up.extend(string_val)
    # Let’s go to the mid value which can be even or odd
    mid = len(split_up) // 2
    for i, _ in enumerate(split_up[:mid+1]):
        split_up[-(i+1)], split_up[i] = split_up[i], split_up[-(i+1)]

    return ''.join(split_up)


def reverse_string2(string_val):
    new = []
    new.extend(string_val)
    new.reverse()
    return ''.join(new)


if __name__ == "__main__":
    s = 'reverse'
    print(reverse_string(s))
    print(reverse_string2(s))
    print(reverse(s))
