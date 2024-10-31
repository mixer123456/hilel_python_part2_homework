from exception import CheapMobPhone


class MobPhone:
    def __init__(self, brand: str, size_h: int, size_w: int, price: int):
        self.brand = brand
        self.__size_h = size_h
        self.__size_w = size_w
        self.__price = price
        if price < 1000:
            raise CheapMobPhone('Mobile phgone is so cheap')

    def __str__(self):
        return f'''
Brand: {self.brand}
Height: {self.__size_h}cm
Wight: {self.__size_w}mm
Price: {self.__price}$
'''

    def getData(self):
        print(f'''
Brand: {self.brand}
Height: {self.__size_h}cm
Wight: {self.__size_w}mm
Price: {self.__price}$
''')

    def get_size_h(self):
        print(f'{self.__size_h}cm')

    def get_size_w(self):
        print(f'{self.__size_w}mm')

    def get_price(self):
        print(f'{self.__price}$')


    def set_size_h(self, new_size_h: int):
        self.__size_h = new_size_h


    def set_size_w(self, new_size_w: int):
        self.__size_w = new_size_w


    def set_price(self, new_price: int):
        self.__price = new_price


mob_phone1 = MobPhone('Apple', 10, 5, 10000)
print(mob_phone1)
mob_phone1.getData()
mob_phone1.get_size_h()
mob_phone1.get_size_w()
mob_phone1.get_price()
mob_phone1.set_size_h(5)
mob_phone1.set_size_w(6)
mob_phone1.set_price(10000000000)
mob_phone1.getData()