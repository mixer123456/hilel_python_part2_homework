vowels_letters = ['a', 'e', 'i', 'o', 'u']

consonants_letters = [
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
    'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',
]


def read_file(file_path: str):
    '''
    read file
    :param file_path: file name
    :return: return data from file
    '''
    with open(file_path, mode='r', encoding='UTF-8') as file:
        return file.read()


def func(file_path: str):
    '''
    calculate count of vowels and count of consonants letters in text and if vowels letters count bigger print top 3
     popular vowels letters or if vowels letters count less that consonants print most popular consonants letter
    :param file_path: file name
    :return: return top 3 popular vowels letter or most popular consonants letter
    '''
    text = read_file(file_path).lower()
    result = {}
    text_vowels = [char for char in text if char in vowels_letters]
    text_consonants = [char for char in text if char in consonants_letters]
    vowels_letters_count = len(text_vowels)
    consonants_letters_count = len(text_consonants)

    if vowels_letters_count > consonants_letters_count:
        for char in vowels_letters:
            result[char] = text.count(char)
        result = list(result.items())
        result.sort(reverse=True, key=lambda char: char[1])
        return result[:3]

    if vowels_letters_count < consonants_letters_count:
        for char in consonants_letters:
            result[char] = text.count(char)
        result = list(result.items())
        result.sort(reverse=True, key=lambda char: char[1])
        return result[0]
