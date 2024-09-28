list1 = [1, 10, 4, 13, 22, 10, 0, 105, 12, 11, 105]


def get_largest_even_number(lst: list) -> int:
    max_even_number = [el for el in lst if el % 2 == 0]

    return max(max_even_number)


result = get_largest_even_number(list1)
print(result)

list2 = [5, 6, 3545, 7547, 243, 9, 37, 98, 22, 57]


def get_three_maximums(lst: list[int]):
    '''
    function get list and return max 3 number from list
    :param lst: function get list
    :return: max 3 number from list
    '''
    unique_values = sorted(set(lst), reverse=True)
    return unique_values[:3]


max_values = get_three_maximums(list2)
print(max_values)
