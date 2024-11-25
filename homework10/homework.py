import re


def is_correct_brackets_in_string(text: str) -> bool:
    '''
    returns True if all brackets in the string have an open and closed pair, but if the bracket does not have a closed or open pair, returns False
    :param text: our text
    :return: True or False
    '''
    text = re.sub(r'[^()\[\]{}]', '', text)
    while '[]' in text or '()' in text or '{}' in text:
        text = text.replace('[]', '').replace('{}', '').replace('()', '')
    return text == ''


text = '[]hbfhbydhyg{}('

test = is_correct_brackets_in_string(Ïtext)
print(test)
