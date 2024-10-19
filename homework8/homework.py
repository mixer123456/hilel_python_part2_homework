def read_file(file_path: str):
    '''
    read file
    :param file_path: file name
    :return: return content from file
    '''
    with open(file_path, mode='r') as file:
        return file.read()


def func(file_path: str):
    '''
    find the most popular and the shortest word in the file
    :param file_path: file name
    :return: return list tuple with the most popular and the shortest word in file
    '''
    text = read_file(file_path).lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '').split()

    #утворюємо сет унікальних слів
    set_text = set(text)

    #перетворюємо його у ліст та сортуруємо його за довжиною слів
    list_text = list(set_text)
    list_text.sort(key=len)

    #берем 1-ий елемент ліста та його довжину
    len_first_el = len(list_text[0])

    #ввидаляємо всі елементи із ліста які довші за вказаний
    list_text = list(filter(lambda el: len_first_el == len(el), list_text))

    # утвворюємо дікт результатів
    dict_text = {}

    #ідем фором по лісту та дообавляєм дикт ключ значення ключ це слово значение це число
    for el in list_text:
        dict_text[el] = text.count(el)

    #з нашего дікта робим список таплів та сортируєм йогоо по кількості
    list_text = list(dict_text.items())
    list_text.sort(reverse=True, key=lambda el: el[1])

    #ввидалити з нашого списка таплів ввсі елементи кількість поовторень яких меньше ніж у першого
    count_first_el = list_text[0][1]
    list_text = list(filter(lambda el: count_first_el == el[1], list_text))

    return list_text


def func2(file_path: str):
    '''
    convert the most popular and the shortest word in the file from lowercase to uppercase
    :param file_path: file name
    :return: returns file in which the most popular and the shortest word is in uppercase
    '''
    text_original = read_file(file_path)
    text = text_original.replace('.', '').replace(',', '').split()
    list_text = func(file_path)
    list_text = [el[0] for el in list_text]
    for el in text:
        if el.lower() in list_text:
            text_original = text_original.replace(f' {el} ', f' {el.upper()} ')
    return text_original


res = func2('input_1.txt')
print(res)
