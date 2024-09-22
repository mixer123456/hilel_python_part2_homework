import math

str1 = 'хакер в реках'


def remove_space(s: str) -> str:
    result = s.replace(' ', '')
    return result

def get_str_revers(s: str) -> str:
    start_ind = len(s) - 1
    result = s[start_ind:0:-1]
    result += s[0]
    return result


def get_half_str_part1(s: str) -> str:
    str_len = len(s)
    half_len = math.ceil(str_len / 2)

    return s[0:half_len]


def get_half_str_part2(s: str) -> str:
    str_len = len(s)
    half_len = math.floor(str_len / 2)

    result = s[half_len:]
    return result

def is_polyndrom(s: str) -> bool:
    s = remove_space(s)
    first_half = get_half_str_part1(s)
    second_half = get_half_str_part2(s)
    second_half = get_str_revers(second_half)
    rs = first_half == second_half
    return rs

t = is_polyndrom(str1)
print(t)


# x = get_half_str_part1(str1)
# d = get_half_str_part2(str1)
# if x == d:
#     print(True)
# else:
#     print(False)
