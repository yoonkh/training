
class Burger:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def info(self):
        print('{}햄버거는 {}원이다'.format(self.name, self.__price))

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price
        print('set new price : ({}원)'.format(self.__price))

