import abc


class Cash(abc.ABC):

    @abc.abstractmethod
    def accept_cash(self, money):
        pass


class CashNormal(Cash):

    def accept_cash(self, money):
        return money


class CashDiscount(Cash):

    def __init__(self, discount):
        self.discount = discount

    def accept_cash(self, money):
        return money * self.discount


class CashReturn(Cash):

    def __init__(self, money_condition=0, money_return=0):
        self.money_condition = money_condition
        self.money_return = money_return

    def accept_cash(self, money):
        if money > self.money_condition:
            return money - (money / self.money_condition) * self.money_return
        return money


class Strategy(object):
    """策略类"""
    def __init__(self, cash):
        self.cash = cash

    def getResult(self, money):
        return self.cash.accept_cash(money)


if __name__ == '__main__':
    strategy1 = Strategy(CashNormal())
    strategy2 = Strategy(CashDiscount(0.8))
    strategy3 = Strategy(CashReturn(100, 10))
    print(strategy1.getResult(95))
    print(strategy2.getResult(95))
    print(strategy3.getResult(195))

