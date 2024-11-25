'''1'''
is_palindrome = lambda s: s == s[::-1]
text = 'maam'
print(is_palindrome(text))  # return True
'''2'''

get_odd_elements = lambda list: [el for el in list if el % 2 != 0]
list_numb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_odd_elements(list_numb))  # return [1, 3, 5, 7, 9]

'''3'''
avg_str_len_list = lambda list: [el for el in list if len(el) <= round(len(''.join(list)) / len(list))]
list1 = ['g', 'rgtg', 'bgvt', 'vfthhy']

print(avg_str_len_list(list1))

