list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for el in list1:
    if el < 5:
        print(el)


list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

set1 = set(list1)
set2 = set(list2)

intersection_set = set1.intersection(set2)

print(list(intersection_set))


list3 = [6, 6, 2, 1, 5, 8, 13, 21, 34, 55, 89]
list4 = [1, 18, 3, 4, 5, 9, 7, 8, 9, 10, 11, 12, 13]

set3 = set(list3)
set4 = set(list4)

symmetric_difference_set = set3.symmetric_difference(set4)

print(list(difference_set))

