def get_gcd(x: int, y: int) -> int:
    '''
    :param x: first integer number
    :param y: second  integer number
    :return: greatest_common_divisor
    '''
    if y == 0:
        return x
    z = x % y
    return get_gcd(y, z)


# result = get_gcd(9, 21)
# print(result)


def func(a: int, b: int) -> list:
    '''
    :param a: first integer number
    :param b: second integer number
    :return:
    '''
    if a == 0 or b == 0:
        return [a, b]
    if a >= 2*b:
        a = a - 2*b
        return func(a, b)
    if b >= 2*a:
        b = b - 2*a
        return func(a, b)
    return [a, b]


result = func(7, 3)
print(result)
