'''1. Створити функцію, яка приймає один список та повертає найбільший парний елемент'''
list1 = [1, 10, 4, 13, 22, 10, 0, 105, 12, 11, 105]

def get_largest_even_number(lst: list) -> int:
    '''
    function get list and return largest even number
    :param lst: function get list
    :return: largest even number
    '''
    max_even_number = [el for el in lst if el % 2 == 0]

    return max(max_even_number)

result = get_largest_even_number(list1)
print(result) # виведе 22


'''2. Створити функцію, яка приймає один список та повертає три максимуми зі списку.'''
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
print(max_values) # виведе  [7547, 3545, 243]


'''Створити функцію, яка приймає два списки і повертає True, якщо в першому списку парних елементів більше, ніж НЕПАРНИХ у другому.'''
list3 = [1, 10, 4, 13, 22, 10, 0, 100, 12, 14, 105]
list4 = [1, 1, 3, 13, 22, 5, 17]

def compare_list(lst1: list, lst2: list):
    '''
    function get 2 lists and compares them
    :param lst1: 1 list
    :param lst2: 2 list
    :return: True or False
    '''
    even_list_1 = [el for el in lst1 if el % 2 == 0]
    odd_list_2 = [el for el in lst2 if el % 2 != 0]

    return len(even_list_1) > len(odd_list_2)

result = compare_list(list3, list4)
print(result) # виведе True
