import re


def read_file(file_path: str):
    '''
    read file
    :param file_path: file name
    :return: return content from file
    '''
    with open(file_path, mode='r') as file:
        return file.read()


def find_most_popular_and_shortest_word(file_path: str):
    '''
    find the most popular and the shortest word in the file
    :param file_path: file name
    :return: return list tuple with the most popular and the shortest word in file
    '''

    text = read_file(file_path)
    text = re.findall(r'\b\w+\b',
                      text.lower())  # використовуємо для розбиття текста на слова з умовою використування символів пунктуації

    # утворюємо сет унікальних слів
    set_text = set(text)

    # перетворюємо його у ліст та сортуруємо його за довжиною слів
    list_text = list(set_text)
    list_text.sort(key=len)

    # берем 1-ий елемент ліста та його довжину
    len_first_el = len(list_text[0])

    # ввидаляємо всі елементи із ліста які довші за вказаний
    list_text = list(filter(lambda el: len_first_el == len(el), list_text))
    print(list_text)

    popular = [(el, text.count(el)) for el in list_text]

    popular.sort(reverse=True, key=lambda el: el[1])

    # ввидалити з нашого списка таплів ввсі елементи кількість поовторень яких меньше ніж у першого
    count_first_el = popular[0][1]
    popular = list(filter(lambda el: count_first_el == el[1], popular))
    print(popular)

    return popular


def convert_from_lowercase_to_uppercase(file_path: str):
    '''
    convert the most popular and the shortest word in the file from lowercase to uppercase
    :param file_path: file name
    :return: returns file in which the most popular and the shortest word is in uppercase
    '''
    text = read_file(file_path)
    words_list = find_most_popular_and_shortest_word(file_path)

    for el in words_list:
        word = el[0]
        pattern = r'\b' + re.escape(word) + r'\b'
        text = re.sub(pattern, word.upper(), text, flags=re.IGNORECASE)

    return text


res = convert_from_lowercase_to_uppercase('input_1.txt')
print(res)
