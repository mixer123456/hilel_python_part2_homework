from exception import CheapMobPhone, SmallOrNegativeSize, BigMobPhone, ExpensiveMobPhone


class MobPhone:
    '''
    Class make template of mobile phone
    '''

    def __init__(self, brand: str, size_h: int, size_w: int, price: int):
        '''
        Initialization method of mobule phone ob'ject
        :param brand: mobile phone brand
        :param size_h: mobile phone height
        :param size_w: mobile phone weight
        :param price: mobile phone price
        '''
        self.brand = brand
        self.size_h = size_h
        self.size_w = size_w
        self.price = price


    def __str__(self):
        '''
        magic method
        :return: data for mob phone
        '''
        return f'''
Brand: {self.brand}
Height: {self.__size_h}cm
Wight: {self.__size_w}mm
Price: {self.__price}$
'''

    __repr__ = __str__

    def getData(self):
        '''
        data of mob phone
        :return: data for mob phone
        '''
        return f'''
Brand: {self.brand}
Height: {self.__size_h}cm
Wight: {self.__size_w}mm
Price: {self.__price}$
'''

    @property
    def size_h(self):
        '''
        get mob phone height
        :return: mob phone height
        '''
        return self.__size_h

    @property
    def size_w(self):
        '''
        get mob phone weight
        :return: mob phone weight
        '''
        return self.__size_w

    @property
    def price(self):
        '''
        get mob phone price
        :return: mob phone price
        '''
        return self.__price

    @size_h.setter
    def size_h(self, new_size_h: int):
        '''
        edit mob phone height
        :param new_size_h: new height for phone
        '''
        if new_size_h < 10:
            raise SmallOrNegativeSize('Mobile phone height is small or with negative height')
        elif new_size_h > 15:
            raise BigMobPhone('Mobile phone height is so big')
        self.__size_h = new_size_h

    @size_w.setter
    def size_w(self, new_size_w: int):
        '''
        edit mob phone weight
        :param new_size_w: new weight for phone
        '''
        if new_size_w < 5:
            raise SmallOrNegativeSize('Mobile phone weight is small or with negative weight')
        elif new_size_w > 10:
            raise BigMobPhone('Mobile phone weight is so big')
        self.__size_w = new_size_w

    @price.setter
    def price(self, new_price: int):
        '''
        edit mob phone price
        :param new_price: new price for phone
        '''
        if new_price <= 450:
            raise CheapMobPhone('Mobile phone is so cheap')
        elif new_price > 5000:
            raise ExpensiveMobPhone('Mobile phone is so expensive')
        self.__price = new_price


mob_phone1 = MobPhone('Apple', 10, 5, 1000)
mob_phone2 = MobPhone('Samsung', 15, 5, 750)
mob_phone3 = MobPhone('Huawei', 13, 10, 3000)
print(mob_phone1)
print(mob_phone1.getData())
print(mob_phone2.getData())
print(mob_phone3.getData())
