class Money:
    def __init__(self, money):
        self.__money = money

    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money
    def get_money(self):
        return self.__money
    def add_money(self, mn):
        res = self.__money + mn.get_money()
        self.__money = res

    @classmethod
    def __check_money(cls, money):
        if money >= 0 and type(money) == int:
            return True
        else:
            return False

