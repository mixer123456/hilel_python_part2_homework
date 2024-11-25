vowels_letters = [
    'a', 'e', 'i', 'o', 'u',
    'а', 'е', 'є', 'и', 'і', 'ї', 'о', 'у', 'ю', 'я',
    'ё', 'ы', 'э',
]

consonants_letters = [
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
    'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',
    'б', 'в', 'г', 'ґ', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н',
    'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ',
]


def read_file(file_path: str):
    '''
    read file
    :param file_path: file name
    :return: return data from file
    '''
    with open(file_path, mode='r', encoding='UTF-8') as file:
        return file.read()


def get_most_popular_letters_in_text(letters: list, text: str, limit: int = 1):
    '''
    get most  popular letters in text
    :param letters: our letters for counting
    :param text: our text for searching letters
    :param limit: limit for top
    :return: return top popular letters in text
    '''
    result = {}

    for char in letters:
        result[char] = text.count(char)  # рахуємо кількість літер у тексті та добавляємо у словник ці літер
    result = list(result.items())  # перетворюємо у ліст щоб можно було йогоо соортувати
    result.sort(reverse=True, key=lambda char: char[1])  # сортуємо за допомогою анонімною фунції
    result = result[:limit]  # робимо тлп найпоопулярніших літер

    return [char[0] for char in result]  # перетворрюємо список таплів у список символів


def get_most_popular_letter_from_file(file_path: str):
    '''
     read text file and calculate count of vowels and count of consonants letters in text and if vowels letters count
     bigger return top 3 popular vowels letters or if vowels letters count less that consonants return most popular
     consonants letter
    :param file_path: file name
    :return: return top 3 popular vowels letter or most popular consonants letter
    '''
    text = read_file(file_path).lower()
    text_vowels = [char for char in text if char in vowels_letters]
    text_consonants = [char for char in text if char in consonants_letters]
    vowels_letters_count = len(text_vowels)
    consonants_letters_count = len(text_consonants)

    if vowels_letters_count > consonants_letters_count:
        return str(get_most_popular_letters_in_text(vowels_letters, text, 3))

    if vowels_letters_count < consonants_letters_count:
        return str(get_most_popular_letters_in_text(consonants_letters, text))

    return 'кількість голоосних дооріввнює кількості приголосних'


def safe_result(file_name: str, result: str):
    '''
    safe result to new file
    :param file_name: file name
    :param result: result that we want safe
    :return: nothing
    '''
    with open(file_name, mode='w') as file:
        file.write(result)


top_letters = get_most_popular_letter_from_file('input_8.txt')
print(top_letters)

safe_result('output.txt', top_letters)
