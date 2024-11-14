from random import shuffle


class Card:
    '''Клас який реалізує методи та властивості гральної стандартної карти'''

    def __init__(self, type: str, k: str):
        '''
        Метод ініціалізації об'єкта карти
        :param type: номінали карти (ACE, KING, QUEEN, JACK ...)
        :param k: масть карти (heart, diamond, club, spades)
        '''
        self.toolType = type  # виклик властимвості сеттера self.__toolType
        self.kit = k  # виклик властимвості сеттера для self.__kit

        self.__SetScore()

    @property
    def toolType(self) -> str:
        '''
                Геттер метод який дозволяє подивитись значення прихованого(інкапсульованого) атрибуту
                :return: рядкове значення номіналу карти
                '''
        return self.__toolType

    @toolType.setter
    def toolType(self, t: str):
        '''
               Сеттер метод для контрольованого та обмеженого доступу до зміни атрибута self.__toolType
               :param t: значення для запису в self.__toolType
               '''
        if t and type(t) is str:
            if t in ("Ace", "King", "Queen", "Jack"):
                self.__toolType = t
            else:
                raise IncorrectCardTypeError(t)
        else:
            raise IncorrectCardTypeError(t)

    @property
    def kit(self) -> str:
        '''
                Геттер метод який дозволяє подивитись значення прихованого(інкапсульованого) атрибуту
                :return: рядкове значення масті карти
                '''
        # return self.__kit
        dict_kit_smiles = {'spades': '♠️', 'heart': '❤️', 'club': '♣️', 'diamond': '♦️'}
        return dict_kit_smiles.get(self.__kit)

    @kit.setter
    def kit(self, k: str):
        '''
               Сеттер метод для контрольованого та обмеженого доступу до зміни атрибута self.__toolType
               :param t: значення для запису в self.__kit
               '''
        if k and type(k) is str:
            if k in ('spades', 'heart', 'club', 'diamond'):
                self.__kit = k
            else:
                raise IncorrectCardKitError(k)
        else:
            raise IncorrectCardKitError(k)

    def __SetScore(self):
        '''
        Метод для створення ваги карт, тобто визначення сенсу карти в грі
        '''
        if self.__toolType == 'Ace':
            self.score = 11
        elif self.__toolType == 'King':
            self.score = 4
        elif self.__toolType == 'Queen':
            self.score = 3
        elif self.__toolType == 'Jack':
            self.score = 2
        else:
            self.score = 0

    def __str__(self) -> str:
        '''
        Метод для відображення карти на екерані
        :return: рядкове представлення об'єкта класу Card
        '''
        # return f'{self.__toolType} {self.__kit}'
        return f'{self.toolType} {self.kit}'

    def __eq__(self, other: 'Card') -> bool:
        '''
        Метод порівння двох карт мід собою, порівннян за масттю та номіналом
        :param other: Інша карта
        :return: логічна відповідь True карти ідентичні, або Flase якщо карти не однакові
        '''
        return self.__toolType == other.__toolType and self.__kit == other.__kit

    __repr__ = __str__


class CardCollection:
    '''Клас який реалізує процеси взаємодії карткових послідовностей(колода, відбій, рука гравця....)'''

    __MAX_COUNT_CARDS = 16
    '''Максимальна кількість карт обумовлена правилами гри'''

    СURRENT_COUNT_CARDS = 0
    '''Атрибут класу для зберігання фактичної кількості карт в картковій послідовності'''

    def __init__(self, n: str):
        '''
        :param n: назва послідовності карт (колода, відбій, рука гравця....)
        '''
        # self.__name = n
        self.setName(n)
        self.cards = []  # контейнер для карт

    def getName(self) -> str:
        '''
        :return:навза карткової послідовності
        '''
        return self.__name.upper()

    def setName(self, n: str):
        '''
        :param n: Приймає в параметрі назву каркової послідовності
        '''
        if n:
            self.__name = n
        else:
            self.__name = None

    def addCard(self, card: 'Card'):
        '''
        :param card: допис нової карти в поточну послідовність карт
        '''
        if CardCollection.СURRENT_COUNT_CARDS + 1 > CardCollection.__MAX_COUNT_CARDS:
            # raise - оператор для виклику виключень при винекненні несанкціонованих подій
            raise CountCardsError(CardCollection.СURRENT_COUNT_CARDS + 1)

        if list(filter(lambda c: c == card, self.cards)):
            raise DoubleCardsError(card)

        CardCollection.СURRENT_COUNT_CARDS += 1
        self.cards.append(card)

    def getNImberOfCards(self) -> int:
        '''
        :return: кількість карт поточної послідовності
        '''
        return len(self.cards)

    def removeCard(self, another_seq: 'CardCollection', card_number: int):
        '''
        Метод для переміщення карти з поточної послідовності карт в another_seq
        :param another_seq: в яку послідовність перемістити карту
        :param card_number: номер карти в поточній послідовнсті, яку необхідно перемістити
        '''

        cart_to_move = None

        if 0 <= card_number < self.getNImberOfCards():
            cart_to_move = self.cards.pop(card_number)
        else:
            print('кАРТУ перемістити не вдалось, ШОСЬ пішло не за планом')
            return None

        another_seq.addCard(cart_to_move)

    def shuffling(self):
        '''Процес тасування карт'''
        shuffle(self.cards)

    def __str__(self) -> str:
        '''
        :return: рядкове представлення карт поточної послідовності
        '''

        str_1 = f'{self.getName()}:\n'

        for i in range(0, self.getNImberOfCards(), 6):
            str_1 += f'\t\t'.join(str(card) for card in self.cards[i:i + 6]) + "\n"

        return str_1


class IncorrectCardTypeError(Exception):
    '''Класс вввиключення для ситуацій з неправильною назвою або типом карти'''

    def __init__(self, t: str):
        '''
        Метод ствворення обʼєкта классу IncorrectCardNameOrTypeError
        :param card:
        '''
        self.message = f'Непавильний тип карти: {t}'

    def __str__(self):
        '''
        Рядкове представлення об'єкта класу IncorrectCardNameOrTypeError
        :return: опис виключення
        '''
        return self.message

class IncorrectCardKitError(Exception):
    def __init__(self, k: str):
        '''
        Метод ствворення обʼєкта классу IncorrectCardKitError
        :param card:
        '''
        self.message = f'Непавильна масть карти: {k}'

    def __str__(self):
        '''
        Рядкове представлення об'єкта класу IncorrectCardKitError
        :return: опис виключення
        '''
        return self.message


class CountCardsError(Exception):
    '''Клас виключення для ситуації перевищення максимально можливої кількості карт в колоді'''

    def __init__(self, count_c: int):
        '''
        Метод створення об'єкта класу CountCardsError
        :param count_c: поточна кількість карт в колоді(за правилами не може бути більше 16)
        '''
        self.message = f'''За поточними правилами гри, кількість карт не повинна перевищувати 16 карт,
але в грі наразі зафіксовано: {count_c}карт'''

    def __str__(self) -> str:
        '''
        Рядкове представлення об'єкта класу CountCardsError
        :return: опис виключення
        '''
        return self.message


class DoubleCardsError(Exception):
    '''Клас виключення для ситуації дублювання карт в колоді'''

    def __init__(self, card: 'Card'):
        '''
        Метод створення об'єкта класу DoubleCardsError
        :param card: поточна карта на додавання в колоду, яка вже й так існує в колоді
        '''
        self.message = f'''За поточними правилами гри, в колоді не може існувати дві однакові карти,
тобто карта {card} вже існує в колоді'''

    def __str__(self) -> str:
        '''
        Рядкове представлення об'єкта класу DoubleCardsError
        :return: опис виключення
        '''
        return self.message


kit = ['heart', 'spades', 'diamond', 'club']
toolType = ['Ace', 'King', 'Queen', 'Jack']

deck = CardCollection('deck')

for tp in toolType:
    for kt in kit:
        deck.addCard(Card(tp, kt))

print(deck)
try:  # оператор для відтворення потенційно небезпечної ділянки коду
    deck.addCard(Card('Ace', 'club'))
    # pass
except CountCardsError:  # блок в якому прописується реакція на конкретне виключення в коді
    # Розв'язок проблеми винекнення виключення
    print(
        'Гравець під ніком ValterEz232134 здійснив спробу додавання в колоду зайвої карти, за це він був виключений з гри')
# except:

# Не обов'зкові блоки
else:  # виконується тільки якщо в try не було виключень
    print('Карта додана успішно в колоду')

finally:  # виконується в будь якому випадку
    deck.shuffling()
    print(deck)

card = Card('Ace', 'heart')
