list1 = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]
list2 = [9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]
list3 = ["a", 0, 0, "b", "c", "d", 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]
list4 = ["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9]
list5 = [0, 1, None, 2, False, 1, 0]
list6 = ["a", "b"]
list7 = ["a"]
list8 = [0, 0]
list9 = [0]
list10 = [False]
list11 = []


def move_zeros_to_end(lst: list):
    '''
    function move zeros to end
    :param lst: get list
    :return: list with zero(-s) at end
    '''
    result = [num for num in lst if not (type(num) is int and num == 0)]
    result += [0] * (len(lst) - len(result))
    return result


result1 = move_zeros_to_end(list1)
print(result1)

result2 = move_zeros_to_end(list2)
print(result2)

result3 = move_zeros_to_end(list3)
print(result3)

result4 = move_zeros_to_end(list4)
print(result4)

result5 = move_zeros_to_end(list5)
print(result5)

result6 = move_zeros_to_end(list6)
print(result6)

result7 = move_zeros_to_end(list7)
print(result7)

result8 = move_zeros_to_end(list8)
print(result8)

result9 = move_zeros_to_end(list9)
print(result9)

result10 = move_zeros_to_end(list10)
print(result10)

result11 = move_zeros_to_end(list11)
print(result11)
