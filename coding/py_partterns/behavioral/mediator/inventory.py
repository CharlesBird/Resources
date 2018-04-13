"""模拟进销存管理"""


import abc
import random


class AbstractCollegue(abc.ABC):

    def __init__(self, mediator):
        self.mediator = mediator


class Purchase(AbstractCollegue):

    def buyIBMcomputer(self, num):
        self.mediator.execute("purchase.buy", num)

    def refuseBuyIBM(self):
        print("不再采购ibm电脑")


class Stock(AbstractCollegue):

    COMPUTER_NUMBER = 100

    def increase(self, num):
        self.COMPUTER_NUMBER = self.COMPUTER_NUMBER + num
        print("库存数量为：%s" % self.COMPUTER_NUMBER)

    def decrease(self, num):
        self.COMPUTER_NUMBER = self.COMPUTER_NUMBER - num
        print("库存数量为：%s" % self.COMPUTER_NUMBER)

    def getStockNumber(self):
        return self.COMPUTER_NUMBER

    def clearStock(self):
        print("清理库存数量为：%s" % self.COMPUTER_NUMBER)
        self.mediator.execute("stock.clear")


class Sale(AbstractCollegue):

    def sellIBMComputer(self, num):
        self.mediator.execute("sale.sell", num)
        print("销售ibm电脑%s台" % num)

    def getSaleStatus(self):
        saleStatus = random.randint(0, 100)
        print("ibm电脑销售情况为：%s" % saleStatus)
        return saleStatus

    def offsale(self):
        self.mediator.execute("sale.offsell")


class AbstractMediator(abc.ABC):

    def __init__(self):
        self.purchase = Purchase(self)
        self.sale = Sale(self)
        self.stock = Stock(self)

    @abc.abstractmethod
    def execute(self, tp, num):
        pass


class Mediator(AbstractMediator):

    def execute(self, tp, num=None):
        if tp == 'purchase.buy':
            self.buyComputer(num)
        elif tp == 'sale.sell':
            self.sellComputer(num)
        elif tp == 'sale.offsell':
            self.offsell()
        elif tp == 'stock.clear':
            self.clearStock()

    def buyComputer(self, num):
        saleStatus = self.sale.getSaleStatus()
        if saleStatus > 80:
            print("采购ibm电脑：%s台" % num)
            self.stock.increase(num)
        else:
            buyNumber = num // 2
            print("采购ibm电脑：%s台" % buyNumber)

    def sellComputer(self, num):
        if self.stock.getStockNumber() < num:
            self.purchase.buyIBMcomputer(num)
        self.stock.decrease(num)

    def offsell(self):
        print("折价销售ibm电脑%s台" % self.stock.getStockNumber())

    def clearStock(self):
        self.sale.offsale()
        self.purchase.refuseBuyIBM()


if __name__ == '__main__':
    mediator = Mediator()
    print("-------采购--------")
    purchase = Purchase(mediator)
    purchase.buyIBMcomputer(100)
    print("-------销售--------")
    sale = Sale(mediator)
    sale.sellIBMComputer(1)
    print("-------库存--------")
    stock = Stock(mediator)
    stock.clearStock()