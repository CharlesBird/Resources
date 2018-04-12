# -*- coding: UTF-8 -*-

# def writefile(file):
# 	f = open(file, 'w')
# 	try:
# 		for num in xrange(1000000000):
# 			f.write(str(num) + '\n')
# 	except Exception, e:
# 		raise e
# 	finally:
# 		f.close()
# writefile('many_num.txt')


# def readfile(file):
# 	f = open(file, 'r')
# 	while True:
# 		try:
# 			line = f.readline()
# 		except Exception, e:
# 			raise e
# 		if not line:
# 			break
# 		yield int(line[:-1])
# print sorted(readfile('many_num.txt'), reverse=True)[:5]

# import os
# import shutil
# res1 = os.makedirs("d:\\1234\\123\\12")
# print res1
# res2 = os.rmdir("d:\\1234\\123\\12")
# print res2
# res3 = os.remove("d:\\1234\\123\\12")
# print res3
# res4 = shutil.rmtree("d:\\1234\\123")
# print res4
# print os.listdir('.')
# print os.walk('.')
# for i in os.walk('.'):
# 	print i

# from sys import getrefcount
# aa = 1
# print getrefcount(aa)
# a = [1, 2, 3]
# print getrefcount(a)
# b = [a, a]
# print getrefcount(a)
# x = a
# print getrefcount(x)
# a = 2
# print getrefcount(x)

# import xmlrpclib
# info = xmlrpclib.ServerProxy('https://demo.odoo.com/start').start()
# url, db, username, password = \
#     info['host'], info['database'], info['user'], info['password']
# print url, db, username, password

# from werkzeug.wrappers import Request, Response
# @Request.application
# def application(request):
#     return Response('Hello World!')

# if __name__ == '__main__':
#     from werkzeug.serving import run_simple
#     run_simple('localhost', 4000, application)

# __new__
# class Singleton(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_inst'):
#             cls._inst = super(Singleton, cls).__new__(cls, *args, **kwargs)
#         return cls._inst
# 修饰器单例模式
# def singleton(cls, *args, **kwargs):
#     instances = {}
#     def _singleton(*args, **kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args, **kwargs)
#         return instances[cls]
#     return _singleton

# class Myclass(Singleton):
#     def __init__(self, x):
#         self.x = x
# one = Myclass(1)
# two = Myclass(2)
# one.x = 5
# two.x = 6
# print id(one), one.x
# print id(two), two.x

# @singleton
# class Myclass2(object):
#     a = 3
#     def __init__(self, x):
#         self.x = x
# one = Myclass2(1)
# two = Myclass2(2)
# one.a = 5
# print id(one), one.x
# print id(two), two.x
# print one.a
# print two.a

# from decimal import Decimal
# a = 2.675
# print Decimal(str(a))
# res = '{:.4f}'.format(Decimal(str(a)))
# print res
# print type(res)

# class Circle(object):
#     def __init__(self, r):
#         self.r = r
#
#     @property
#     def area(self):
#         return 3.14 * self.r ** 2
#
# c = Circle(6)
# print c.area

# class lazy_property(object):
#     def __init__(self, func):
#         self.func = func
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         value = self.func(instance)
#         setattr(instance, self.func.__name__, value)
#         return value
#
# class Circle(object):
#     def __init__(self, r):
#         self.r = r
#
#     @lazy_property
#     def area(self):
#         print 'evalute'
#         return 3.14 * self.r ** 2
#
# c = Circle(6)
# print 'before first visit'
# print c.__dict__
# print c.area
# print 'after first visit'
# print c.__dict__
# print c.area

# 简单的工厂模式
# class Circle(object):
#     def draw(self):
#         print 'draw circle'
# class Rectangle(object):
#     def draw(self):
#         print 'draw Rectangle'
# class ShapeFactory(object):
#     def create(self, shape):
#         if shape == 'Circle':
#             return Circle()
#         if shape == 'Rectangle':
#             return ShapeFactory()
# sf = ShapeFactory()
# obj = sf.create('Circle')
# obj.draw()

# 适配器模式
# class Target(object):
#     def request(self):
#         print 'common request.'
# class Adaptee(Target):
#     def specificRequest(self):
#         print 'specific request.'
# class Adapter(Target):
#     def __init__(self, ada):
#         self.ada = ada
#     def request(self):
#         self.ada.specificRequest()
# ada = Adaptee()
# adapter = Adapter(ada)
# adapter.request()

# 适配器模式
# class Dog(object):
#     def __init__(self):
#         self.name = "Dog"
#
#     def bark(self):
#         return "woof!"
#
#
# class Cat(object):
#     def __init__(self):
#         self.name = "Cat"
#
#     def meow(self):
#         return "meow!"
#
#
# class Human(object):
#     def __init__(self):
#         self.name = "Human"
#
#     def speak(self):
#         return "'hello'"
#
#
# class Car(object):
#     def __init__(self):
#         self.name = "Car"
#
#     def make_noise(self, octane_level):
#         return "vroom%s" % ("!" * octane_level)
#
#
# class Adapter(object):
#     """
#     Adapts an object by replacing methods.
#     Usage:
#     dog = Dog
#     dog = Adapter(dog, dict(make_noise=dog.bark))
#     """
#     def __init__(self, obj, adapted_methods):
#         """We set the adapted methods in the object's dict"""
#         self.obj = obj
#         self.__dict__.update(adapted_methods)
#
#     def __getattr__(self, attr):
#         """All non-adapted calls are passed to the object"""
#         return getattr(self.obj, attr)
#
# def main():
#     objects = []
#     dog = Dog()
#     objects.append(Adapter(dog, dict(make_noise=dog.bark)))
#     cat = Cat()
#     objects.append(Adapter(cat, dict(make_noise=cat.meow)))
#     human = Human()
#     objects.append(Adapter(human, dict(make_noise=human.speak)))
#     car = Car()
#     car_noise = lambda: car.make_noise(3)
#     objects.append(Adapter(car, dict(make_noise=car_noise)))
#
#     for obj in objects:
#         print("A", obj.name, "goes", obj.make_noise())
#
# if __name__ == "__main__":
#     main()


# class DrawingAPI1(object):
#     def draw_circle(self, x, y, radius):
#         print('API1.circle at {}:{} radius {}'.format(x, y, radius))
# class DrawingAPI2(object):
#     def draw_circle(self, x, y, radius):
#         print('API2.circle at {}:{} radius {}'.format(x, y, radius))
# class CircleShape(object):
#     def __init__(self, x, y, radius, drawing_api):
#         self._x = x
#         self._y = y
#         self._radius = radius
#         self._drawing_api = drawing_api
#
#     def draw(self):
#         self._drawing_api.draw_circle(self._x, self._y, self._radius)
#
#     def scale(self, pct):
#         self._radius *= pct
#
# def main():
#     shapes = (
#         CircleShape(1, 2, 3, DrawingAPI1()),
#         CircleShape(5, 7, 11, DrawingAPI2())
#     )
#
#     for shape in shapes:
#         shape.scale(2.5)
#         shape.draw()
#
# if __name__ == '__main__':
#     main()

# def printInfo(info):
#   print unicode(info, 'utf-8').encode('utf-8')
#
# #抽象类：手机品牌
# class HandsetBrand():
#   soft = None
#   def SetHandsetSoft(self, soft):
#     self.soft = soft
#   def Run(self):
#     pass
#
# #具体抽象类：手机品牌1
# class HandsetBrand1(HandsetBrand):
#   def Run(self):
#     printInfo('手机品牌1:')
#     self.soft.Run()
#
# #具体抽象类：手机品牌2
# class HandsetBrand2(HandsetBrand):
#   def Run(self):
#     printInfo('手机品牌2:')
#     self.soft.Run()
#
# #功能类：手机软件
# class HandsetSoft():
#   def Run(self):
#     pass
#
# #具体功能类：游戏
# class HandsetGame(HandsetSoft):
#   def Run(self):
#     printInfo('运行手机游戏')
#
# #具体功能类：通讯录
# class HandsetAddressList(HandsetSoft):
#   def Run(self):
#     printInfo('运行手机通信录')
#
# def clientUI():
#   h1 = HandsetBrand1()
#   h1.SetHandsetSoft(HandsetAddressList())
#   h1.Run()
#   h1.SetHandsetSoft(HandsetGame())
#   h1.Run()
#
#   h2 = HandsetBrand2()
#   h2.SetHandsetSoft(HandsetAddressList())
#   h2.Run()
#   h2.SetHandsetSoft(HandsetGame())
#   h2.Run()
#   return
#
# if __name__ == '__main__':
#   clientUI()

# 桥接模式
# class TravelForm(object):
#     def __init__(self, form="stay at home"):
#         self.form = form
#     def getForm(self):
#         return self.form
# class Group(TravelForm):
#     def __init__(self, form="by group"):
#         super(Group, self).__init__(form)
# class Independent(TravelForm):
#     def __init__(self, form="by myself"):
#         super(Independent, self).__init__(form)
# class Destination(object):
#     def __init__(self, info):
#         self.info = info
#     def setForm(self, form):
#         self.form = form
#     def getInfo(self):
#         print (self.info + " " + self.form.getForm())
# class DaLian(Destination):
#     def __init__(self, info="Go to DaLian"):
#         super(DaLian, self).__init__(info)
# class ShangHai(Destination):
#     def __init__(self, info="Go to ShangHai"):
#         super(ShangHai, self).__init__(info)
# if __name__ == '__main__':
#     destination = ShangHai()
#     destination.setForm(Group())
#     destination.getInfo()
#
#     destination = DaLian()
#     destination.setForm(Independent())
#     destination.getInfo()

# 建造者模式
# class Director(object):
#     def __init__(self):
#         self.builder = None
#     def construct_building(self):
#         self.builder.new_building()
#         self.builder.build_floor()
#         self.builder.build_size()
#     def get_building(self):
#         return self.builder.building
# class Builder(object):
#     def __init__(self):
#         self.building = None
#     def new_building(self):
#         self.building = Building()
# class BuilderHouse(Builder):
#     def build_floor(self):
#         self.building.floor = 'One'
#     def build_size(self):
#         self.building.size = 'Big'
# class BuilderFlat(Builder):
#     def build_floor(self):
#         self.building.floor = 'More than One'
#     def build_size(self):
#         self.building.size = 'Small'
# class Building(object):
#     def __init__(self):
#         self.floor = None
#         self.size = None
#     def __repr__(self):
#         return 'Floor: %s | Size: %s' % (self.floor, self.size)
# if __name__ == "__main__":
#     director = Director()
#     director.builder = BuilderHouse()
#     director.construct_building()
#     building = director.get_building()
#     print(building)
#     director.builder = BuilderFlat()
#     director.construct_building()
#     building = director.get_building()
#     print(building)

# def printInfo(info):
#     print unicode(info, 'utf-8').encode('utf-8')
#
# #建造者基类
# class PersonBuilder():
#     def BuildHead(self):
#         pass
#
#     def BuildBody(self):
#         pass
#
#     def BuildArm(self):
#         pass
#
#     def BuildLeg(self):
#         pass
#
# #胖子
# class PersonFatBuilder(PersonBuilder):
#     type = '胖子'
#     def BuildHead(self):
#         printInfo("构建%s的头" % self.type)
#
#     def BuildBody(self):
#         printInfo("构建%s的身体" % self.type)
#
#     def BuildArm(self):
#         printInfo("构建%s的手" % self.type)
#
#     def BuildLeg(self):
#         printInfo("构建%s的脚" % self.type)
#
#
# #瘦子
# class PersonThinBuilder(PersonBuilder):
#     type = '瘦子'
#     def BuildHead(self):
#         printInfo("构建%s的头" % self.type)
#
#     def BuildBody(self):
#         printInfo("构建%s的身体" % self.type)
#
#     def BuildArm(self):
#         printInfo("构建%s的手" % self.type)
#
#     def BuildLeg(self):
#         printInfo("构建%s的脚" % self.type)
#
# #指挥者
# class PersonDirector():
#     pb = None;
#     def __init__(self, pb):
#         self.pb = pb
#
#     def CreatePereson(self):
#         self.pb.BuildHead()
#         self.pb.BuildBody()
#         self.pb.BuildArm()
#         self.pb.BuildLeg()
#
# def clientUI():
#     pb = PersonThinBuilder()
#     pd = PersonDirector(pb)
#     pd.CreatePereson()
#
#     pb = PersonFatBuilder()
#     pd = PersonDirector(pb)
#     pd.CreatePereson()
#     return
# if __name__ == '__main__':
#     clientUI()

# 职责链模式
# 抽象职责类
# class Manager(object):
#     successor = None
#     name = ''
#     def __init__(self, name):
#         self.name = name
#
#     def setSuccessor(self, successor):
#         self.successor = successor
#
#     def handleRequest(self, request):
#         pass
#
# #具体职责类：经理
# class CommonManager(Manager):
#     def handleRequest(self, request):
#         if request.RequestType == '请假' and request.Number <= 2:
#             print '%s:%s 数量%d 被批准' % (self.name, request.RequestContent, request.Number)
#         else:
#             if self.successor != None:
#                 self.successor.handleRequest(request)
#
# #具体职责类：总监
# class Majordomo(Manager):
#     def handleRequest(self, request):
#         if request.RequestType == '请假' and request.Number <= 5:
#             print '%s:%s 数量%d 被批准' % (self.name, request.RequestContent, request.Number)
#         else:
#             if self.successor != None:
#                 self.successor.handleRequest(request)
#
# #具体职责类：总经理
# class GeneralManager(Manager):
#     def handleRequest(self, request):
#         if request.RequestType == '请假':
#             print '%s:%s 数量%d 被批准' % (self.name, request.RequestContent, request.Number)
#         elif request.RequestType == '加薪' and request.Number <= 500:
#             print '%s:%s 数量%d 被批准' % (self.name, request.RequestContent, request.Number)
#         elif request.RequestType == '加薪' and request.Number > 500:
#             print '%s:%s 数量%d 再说吧' % (self.name, request.RequestContent, request.Number)
#         else:
#             if self.successor != None:
#                 self.successor.handleRequest(request)
#
# class Request():
#     RequestType = ''
#     RequestContent = ''
#     Number = 0
#
# def clientUI():
#     jinLi = CommonManager('金力')
#     zongJian = Majordomo('宗健')
#     zhongJingLi = GeneralManager('钟金利')
#
#     jinLi.setSuccessor(zongJian)
#     zongJian.setSuccessor(zhongJingLi)
#
#     request = Request()
#     request.RequestType = '请假'
#     request.RequestContent = '小菜请假'
#     request.Number = 1
#     jinLi.handleRequest(request)
#
#     request.RequestType = '请假'
#     request.RequestContent = '小菜请假'
#     request.Number = 5
#     jinLi.handleRequest(request)
#
#     request.RequestType = '加薪'
#     request.RequestContent = '小菜要求加薪'
#     request.Number = 500
#     jinLi.handleRequest(request)
#
#     request.RequestType = '加薪'
#     request.RequestContent = '小菜要求加薪'
#     request.Number = 1000
#     jinLi.handleRequest(request)
#     return
#
# if __name__ == '__main__':
#     clientUI()


# import time
# #Command
# class Command():
#     receiver = None
#     def __init__(self, receiver):
#         self.receiver = receiver
#
#     def Execute(self):
#         pass
#
# #具体命令类：拷羊肉串
# class BakeMuttonCommand(Command):
#     def SetHandsetSoft(self, receiver):
#         Command.__init__(self,receiver)
#
#     def Execute(self):
#         self.receiver.BakeMutton()
#
#     def ToString(self):
#         return '拷羊肉串'
#
#
# #具体命令类：拷鸡翅
# class BakeChickenWingCommand(Command):
#     def SetHandsetSoft(self, receiver):
#         Command.__init__(self,receiver)
#
#     def Execute(self):
#         self.receiver.BakeChickenWing()
#
#     def ToString(self):
#         return '拷鸡翅'
#
# #Receiver：拷肉串的人
# class Barbecuer():
#     def BakeChickenWing(self):
#         print ('拷鸡翅！')
#
#     def BakeMutton(self):
#         print ('拷羊肉串！')
#
# #Invoker：服务员
# class Waiter():
#     commandList = []
#
#     def SetOrder(self,command):
#         print ('%s 增加订单：%s' % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),command.ToString()))
#         self.commandList.append(command)
#
#     def CancelOrder(self,command):
#         print ('%s 取消订单：%s' % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),command.ToString()))
#         self.commandList.remove(command)
#
#     def Notify(self):
#         print ('\n通知：')
#         for command in self.commandList:
#             command.Execute()
#
#     def Run(self):
#         print ('运行手机通信录')
#
# def clientUI():
#     boy = Barbecuer()
#     bakeMuttonCommand1 = BakeMuttonCommand(boy)
#     bakeMuttonCommand2 = BakeMuttonCommand(boy)
#     bakeChickenWingCommand1 = BakeChickenWingCommand(boy)
#     girl = Waiter()
#
#     girl.SetOrder(bakeMuttonCommand1)
#     girl.SetOrder(bakeMuttonCommand2)
#     girl.SetOrder(bakeChickenWingCommand1)
#     girl.CancelOrder(bakeMuttonCommand1)
#     girl.Notify()
#     return
#
# if __name__ == '__main__':
#     clientUI()


# Component：公司抽象类
# class Company:
#     name = ''
#     def __init__(self, name):
#         self.name = name
#
#     def Add(self, company):
#         pass
#
#     def Remove(self, company):
#         pass
#
#     def Display(self, depth):
#         pass
#
#     def LineOfDuty(self): #履行职责
#         pass
#
# #Composite：公司类
# class ConcreteCompany(Company):
#     childrenCompany = None
#
#     def __init__(self, name):
#         Company.__init__(self,name)
#         self.childrenCompany = []
#
#     def Add(self, company):
#         self.childrenCompany.append(company)
#
#     def Remove(self, company):
#         self.childrenCompany.remove(company)
#
#     def Display(self, depth):
#         print ('-'*depth + self.name)
#
#         for component in self.childrenCompany:
#             component.Display(depth+2)
#
#
#     def LineOfDuty(self): #履行职责
#         for component in self.childrenCompany:
#             component.LineOfDuty()
#
# #Leaf：具体职能部门
# class HRDepartment(Company):
#     def __init__(self, name):
#          Company.__init__(self,name)
#
#     def Display(self, depth):
#         print ('-'*depth + self.name)
#
#     def LineOfDuty(self): #履行职责
#         print ('%s\t员工招聘培训管理' % self.name)
#
# #Leaf：具体职能部门
# class FinanceDepartment(Company):
#     def __init__(self, name):
#         Company.__init__(self,name)
#
#     def Display(self, depth):
#         print ('-'*depth + self.name)
#
#     def LineOfDuty(self): #履行职责
#         print ('%s\t公司财务收支管理' % self.name)
#
# def clientUI():
#     root = ConcreteCompany('北京总公司')
#     root.Add(HRDepartment('总公司人力资源部'))
#     root.Add(FinanceDepartment('总公司财务部'))
#
#     comp = ConcreteCompany('华东分公司')
#     comp.Add(HRDepartment('华东分公司人力资源部'))
#     comp.Add(FinanceDepartment('华东分公司财务部'))
#     root.Add(comp)
#
#     comp1 = ConcreteCompany('南京办事处')
#     comp1.Add(HRDepartment('南京办事处人力资源部'))
#     comp1.Add(FinanceDepartment('南京办事处财务部'))
#     comp.Add(comp1)
#
#     comp2 = ConcreteCompany('杭州办事处')
#     comp2.Add(HRDepartment('杭州办事处人力资源部'))
#     comp2.Add(FinanceDepartment('杭州办事处财务部'))
#     comp.Add(comp2)
#
#     print ('-------公司结构图-------')
#     root.Display(1)
#
#     print ('\n-------职责-------')
#     root.LineOfDuty()
#     return
#
# if __name__ == '__main__':
#     clientUI()


# class foo(object):
#     def f1(self):
#         print("original f1")
#
#     def f2(self):
#         print("original f2")
#
#
# class foo_decorator(object):
#     def __init__(self, decoratee):
#         self._decoratee = decoratee
#
#     def f1(self):
#         print("decorated f1")
#         self._decoratee.f1()
#
#     def __getattr__(self, name):
#         return getattr(self._decoratee, name)
#
# u = foo()
# v = foo_decorator(u)
# v.f1()
# v.f2

# class Beverage:
#     description = "Unknown Beverage"
#
#     def get_description(self):
#         return self.description
#
#     def cost(self):
#         pass
#
#
# class CondimentDecorator(Beverage):
#     def get_description(self):
#         pass
#
#
# class MilkyTea(Beverage):
#     def __init__(self):
#         self.description = "MilkyTea"
#
#     def cost(self):
#         return 1.99
#
#
# class FruitJuice(Beverage):
#     def __init__(self):
#         self.description = "FruitJuice"
#
#     def cost(self):
#         return 1.80
#
#
# class Coffee(Beverage):
#     def __init__(self):
#         self.description = "Coffee"
#
#     def cost(self):
#         return 2.00
#
#
# class Pearl(CondimentDecorator):
#     def __init__(self, beverage):
#         self.beverage = beverage
#
#     def get_description(self):
#         return self.beverage.get_description() + " + Pearl"
#
#     def cost(self):
#         return 1.50 + self.beverage.cost()
#
#
# class Pudding(CondimentDecorator):
#     def __init__(self, beverage):
#         self.beverage = beverage
#
#     def get_description(self):
#         return self.beverage.get_description() + " + Pudding"
#
#     def cost(self):
#         return 1.60 + self.beverage.cost()
#
#
# class Milk(CondimentDecorator):
#     def __init__(self, beverage):
#         self.beverage = beverage
#
#     def get_description(self):
#         return self.beverage.get_description() + " + Milk"
#
#     def cost(self):
#         return 2.10 + self.beverage.cost()
#
#
# if __name__ == '__main__':
#     b = FruitJuice()
#     print "%s = $%s\n" % (b.get_description(), b.cost())
#
#     b = MilkyTea()
#     b = Pearl(b)
#     b = Pudding(b)
#     print "%s = $%s\n" % (b.get_description(), b.cost())
#
#     b = Coffee()
#     b = Pearl(b)
#     b = Milk(b)
#     print "%s = $%s\n" % (b.get_description(), b.cost())

# class foo():
#     def __str__(self):
#         return 'test str'
#     def __repr__(self):
#         return 'test repr'
# f = foo()
# print f

# class Pizza:
#     name = ""
#     dough = ""
#     sauce = ""
#     toppings = []
#
#     def prepare(self):
#         print "Preparing %s" % self.name
#         print "    dough: %s" % self.dough
#         print "    sauce: %s" % self.sauce
#         print "    add toppings:"
#         for n in self.toppings:
#             print "        %s" % n
#
#     def bake(self):
#         print "Bake for 25 minutes at 350."
#
#     def cut(self):
#         print "Cutting into diagonal slices."
#
#     def box(self):
#         print "Put into official box."
#
#     def get_name(self):
#         return self.name
#
#
# class PizzaStore:
#     def order_pizza(self, pizza_type):
#         self.pizza = self.create_pizza(pizza_type)
#         self.pizza.prepare()
#         self.pizza.bake()
#         self.pizza.cut()
#         self.pizza.box()
#         return self.pizza
#
#     def create_pizza(self, pizza_type):
#         pass
#
#
# class NYStyleCheesePizza(Pizza):
#     def __init__(self):
#         self.name = "NY Style Cheese Pizza"
#         self.dough = "NY Dough"
#         self.sauce = "NY Sauce"
#         self.toppings.append("NY toopping A")
#         self.toppings.append("NY toopping B")
#
#
# class ChicagoStyleCheesePizza(Pizza):
#     def __init__(self):
#         self.name = "Chicago Style Cheese Pizza"
#         self.dough = "Chicago Dough"
#         self.sauce = "Chicago Sauce"
#         sefl.toppings.append("Chicago toopping A")
#
#     def cut(self):
#         print "Cutting into square slices."
#
#
# class NYStyleClamPizza(Pizza):
#     def __init__(self):
#         self.name = "NY Style Clam Pizza"
#         self.dough = "NY Dough"
#         self.sauce = "NY Sauce"
#         self.toppings.append("NY toopping A")
#         self.toppings.append("NY toopping B")
#
#
# class ChicagoStyleClamPizza(Pizza):
#     def __init__(self):
#         self.name = "Chicago Style Clam Pizza"
#         self.dough = "Chicago Dough"
#         self.sauce = "Chicago Sauce"
#         self.toppings.append("Chicago toopping A")
#
#     def cut(self):
#         print "Cutting into square slices."
#
#
# class NYPizzaStore(PizzaStore):
#     def create_pizza(self, pizza_type):
#         if pizza_type == "cheese":
#             return NYStyleCheesePizza()
#         elif pizza_type == "clam":
#             return NYStyleClamPizza()
#         else:
#             return None
#
#
# class ChicagoPizzaStore(PizzaStore):
#     def create_pizza(self, pizza_type):
#         if pizza_type == "cheese":
#             return ChicagoStyleCheesePizza()
#         elif pizza_type == "clam":
#             return ChicagoStyleClamPizza()
#         else:
#             return None
#
# if __name__ == "__main__":
#     ny_store = NYPizzaStore()
#     chicago_store = ChicagoPizzaStore()
#
#     pizza = ny_store.order_pizza("cheese")
#     print "Mike ordered a %s." % pizza.get_name()
#     print
#
#     pizza = chicago_store.order_pizza("clam")
#     print "John ordered a %s." % pizza.get_name()
#     print

# import requests
# import urllib
# from cachecontrol import CacheControl
# headers = {'content-type': 'application/json'}
# data = {'username': 'ok', 'passwd': 'python', 'method': 'erp.stock.inventory.get', 'skuList': ['P0037873', 'P0037874', 'P0037872', 'P0037875']}
# data = {'username': 'flask', 'passwd': 'python', 'method': 'create.product.attribute.value', 'value': {'code': 'code1', 'name': 'name1', 'remark': 'remark'}}
# data = {'username': 'flask', 'passwd': 'python'}
# with requests.session() as s:
#     cache_s = CacheControl(s)
# r = cache_s.get('https://passport.baidu.com/v2', auth=(urllib.quote('轻迹天下'), '5377343zhon'))
# r = cache_s.post('http://dev-api.newbeemall.com/v1.0/rest2', json=data, headers=headers)
# print dir(r)
# print r.__dict__
# print r.json()
# print r.headers, r.encoding
# print r.text
# print r.cookies

# import unittest2
# import unittest

# class TestStringMethods(unittest2.TestCase):
#
#   def test_upper(self):
#       self.assertEqual('foo'.upper(), 'FOO')
#
#   def test_isupper(self):
#       self.assertTrue('FOO'.isupper())
#       self.assertTrue('Foo'.isupper())
#
#   def test_split(self):
#       s = 'hello world'
#       self.assertEqual(s.split(), ['hello', 'world'])
#       # check that s.split fails when the separator is not a string
#       with self.assertRaises(TypeError):
#           s.split(2)
#
# if __name__ == '__main__':
#     unittest2.main()

# class Widget:
#     def __init__(self, size = (40, 40)):
#         self._size = size
#     def getSize(self):
#         return self._size
#     def resize(self, width, height):
#         if width < 0  or height < 0:
#             raise ValueError, "illegal size"
#         self._size = (width, height)
#     def dispose(self):
#         pass

# class WidgetTestCase(unittest2.TestCase):
#     def setUp(self):
#         self.widget = Widget()
#     def tearDown(self):
#         self.widget = None
#     def testSize(self):
#         self.assertEqual(self.widget.getSize(), (40, 40))
# # 构造测试集
# def suite():
#     suite = unittest2.TestSuite()
#     suite.addTest(WidgetTestCase("testSize"))
#     return suite
# # 测试
# if __name__ == "__main__":
#     unittest2.main(defaultTest='suite')

# from socket import *
# from time import ctime

# host = gethostbyname(gethostname())
# port = 21567
# bufsize = 1024
# addr = (host, port)
# tcpskt = socket(AF_INET, SOCK_STREAM)
# tcpskt.bind(addr)
# tcpskt.listen(5)
# while 1:
#     print 'waiting for connection ...'
#     tcpcliskt, cliaddr = tcpskt.accept()
#     print '... connected from: ', cliaddr
#     data = tcpcliskt.recv(bufsize)
#     if not data:
#         break
#     tcpcliskt.send('%s, %s' % (ctime(), data))
#     print [ctime()], ':', data
#     tcpcliskt.close()
# tcpskt.close()

# from socket import *
# host = '192.168.223.128'
# port = 15158
# bufsize = 1024
# addr = (host, port)
# tcpcliskt = socket(AF_INET, SOCK_STREAM)
# tcpcliskt.connect(addr)
# while 1:
#     data = 'client test1'
#     # if not data:
#     #     break
#     tcpcliskt.send(data)
#     data2 = tcpcliskt.recv(bufsize)
#     # if not data:
#     #     break
#     print data2
# # tcpcliskt.close()

# method = 'oms.order.return.list.get'
# timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
# page = 1
# page_size = 10
# format = 'json'
# key = 'afd9ba3822f636d314e7cc1142852c32'
# v = '2.0'
# sign_method = 'md5'
# kh_id = 2278
# import time
# import requests
# import json
# headers = {'content-type': 'application/json'}
# args = dict(method='prm.goods.spec1.update', timestamp=time.strftime('%Y-%m-%d %H:%M:%S'), format='json', key='afd9ba3822f636d314e7cc1142852c32', v='2.0', sign_method='md5')
# args.update({'spec1_code': 'code1', 'spec1_name': '测试'})
# secret = '355eabf36cf79ec164bae015ec9601f4'
# url = 'http://121.199.164.211/chengdu/webefast/web/?app_act=openapi/router'
# def get_sign(secret, args):
#     assert(isinstance(args, dict)), 'type error!!!'
#     tmp = secret
#     for key, val in sorted(args.iteritems(), key=lambda d: d[0], reverse=False):
#         if val:
#             tmp += key + val
#     tmp += secret
#     try:
#         import hashlib
#         hash = hashlib.md5()
#     except ImportError:
#         # for Python << 2.5
#         import md5
#         hash = md5.new()
#     hash.update(tmp)
#     res = hash.hexdigest().upper()
#     return res
# args.update({'sign': get_sign(secret, args)})
# respon = requests.post(url, params=args, headers=headers)
# print respon.__dict__
# r = json.loads(respon.text)
# print r
# print r['message']


# try:
#     import cPickle as pickle
# except:
#     import pickle
# import StringIO
# class Person(object):
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#     def display(self):
#         print 'name:', self.name, 'address:', self.address
# jj = Person("JGood", "中国 杭州")
# jj.display()
# file = StringIO.StringIO()
# pickle.dump(jj, file, 2)
# file.seek(0)
# jj1 = pickle.load(file)
# jj1.display()
# file.close()

# class MyClass(object):
#     x = 1
#     def func(self, param):
#         pass
#     pass
# print dir(MyClass)
# class MyClass2:
#     __metaclass__ = type
#     x = 1
#     def func(self):
#         pass
# print dir(MyClass2)
# print type(MyClass)
# print type(MyClass())
# print MyClass.__class__
# print MyClass().__class__
# print MyClass.__bases__
#
# def Foo():
#     return 1
# print Foo.__class__
# import inspect
# print inspect.ismethod(MyClass().func)
# print inspect.isroutine(Foo)

# def gen(a, b, c, *args, **kwargs):
#     for i in range(5):
#         yield i
# g = gen()
# print g.gi_code
# print g.gi_frame
# print g.gi_running
# print g.next()
# for j in g:
#     print j
# c = gen.func_code
# print c.co_argcount
# print c.co_varnames
# print c.co_filename
# print c.co_flags
# co = MyClass().func.func_code
# print co.co_argcount
# print co.co_varnames
# print co.co_filename
# print co.co_flags

# import sys
# def div(a, b):
#     try:
#         return a / b
#     except:
#         tb = sys.exc_info()[2]
#         print sys.exc_info()
#         print tb
#         print tb.tb_lineno
#         print tb.tb_frame
#         print tb.tb_next
# div(1, 0)

# def ma(cls):
#     print 'method a'
#
#
# def mb(cls):
#     print 'method b'
#
# method_dict = {
#     'ma': ma,
#     'mb': mb,
# }
#
#
# class DynamicMethod(type):
#
#     def __new__(cls, name, bases, dct):
#         if name[:3] == 'Abc':
#             dct.update(method_dict)
#         return type.__new__(cls, name, bases, dct)
#
#     def __init__(cls, name, bases, dct):
#         super(DynamicMethod, cls).__init__(name, bases, dct)
#
#
# class AbcTest(object):
#     __metaclass__ = DynamicMethod
#
#     x = 3
#     def mc(self, x):
#         print x * 3
#
#
# class NotAbc(object):
#     __metaclass__ = DynamicMethod
#
#     def md(self, x):
#         print x * 3
#
# a = AbcTest()
# a.mc(3)
# a.ma()
# print dir(a)
#
# b = NotAbc()
# print dir(b)

# import xmlrpclib
# def test_db(host, port, method, *args):
#     uri = 'http://' + host + ':' + port
#     conn = xmlrpclib.ServerProxy(uri + '/xmlrpc/db')
#     res = getattr(conn, method)(*args)
#     return res

# print test_db('192.168.3.49', '8069', 'dump', 'guotao@123', 'zhc_0809')

# import threading
# import time
# def foo():
#     for i in range(100):
#         print i
#         time.sleep(1)

# def test():
#     t = threading.Thread(target=foo, args=())
#     t.start()

# def foo2():
#     print 'before'
#     test()
#     print 'after'
# foo2()

# def gen():
#     for i in range(10):
#         yield i

# def f0(*args, **kwargs):
#     print kwargs['x'] + kwargs['y']

# def f1(*args, **kwargs):
#     a, b = args
#     f0(*args, **kwargs)
#     return a + b

# def f2(*args, **kwargs):
#     x, y, z = args
#     print list(z)
#     return args

# print f2(2, 3, gen())

# def decorator(F):
#     def new_F(*args, **kwargs):
#         print args
#         res = F(*args, **kwargs)
#         if res:
#             print '234554'
#         else:
#             print '1213123'
#     return new_F

# class A(object):
#     def foo(self, a, b):
#         return a, b
#     @classmethod
#     def foo2(cls, a, b):
#         print object.__new__(cls)
#         print 'foo2', cls
#         return a, b
#     @staticmethod
#     def foo3(a, b):
#         return a, b
# class B(A):
#     @decorator
#     def foo(self, a, b):
#         res = super(B, self).foo(a, b)
#         return res
# print A.foo3(6, 7)
# print A.foo2(4, 5)
# a = A()
# print a.foo(2, 4)
# print a.foo2(4, 8)
# b = B()
# print b.foo(1, 3)

# import random
# from time import sleep
# from greenlet import greenlet
# from Queue import Queue

# queue = Queue(1)

# @greenlet
# def producer():
#     chars = ['a', 'b', 'c', 'd', 'e']
#     global queue
#     while True:
#         char = random.choice(chars)
#         queue.put(char)
#         print "Produced: ", char
#         sleep(1)
#         consumer.switch()

# @greenlet
# def consumer():
#     global queue
#     while True:
#         char = queue.get()
#         print "Consumed: ", char
#         sleep(1)
#         producer.switch()

# if __name__ == "__main__":
#     producer.run()
#     consumer.run()

# from PIL import Image, ImageDraw, ImageEnhance
# im = Image.open("veriCode2.jpg")
# im = ImageEnhance.Sharpness(im).enhance(3)


# def getPixel(image, x, y, G, N):
#     L = image.getpixel((x, y))
#     if L > G:
#         L = True
#     else:
#         L = False

#     nearDots = 0
#     if L == (image.getpixel((x - 1, y - 1)) > G):
#         nearDots += 1
#     if L == (image.getpixel((x - 1, y)) > G):
#         nearDots += 1
#     if L == (image.getpixel((x - 1, y + 1)) > G):
#         nearDots += 1
#     if L == (image.getpixel((x, y - 1)) > G):
#         nearDots += 1
#     if L == (image.getpixel((x, y + 1)) > G):
#         nearDots += 1
#     if L == (image.getpixel((x + 1, y - 1)) > G):
#         nearDots += 1
#     if L == (image.getpixel((x + 1, y)) > G):
#         nearDots += 1
#     if L == (image.getpixel((x + 1, y + 1)) > G):
#         nearDots += 1

#     if nearDots < N:
#         return image.getpixel((x, y - 1))
#     else:
#         return None

# 降噪
# 根据一个点A的RGB值，与周围的8个点的RBG值比较，设定一个值N（0 <N <8），当A的RGB值与周围8个点的RGB相等数小于N时，此点为噪点
# G: Integer 图像二值化阀值
# N: Integer 降噪率 0 <N <8
# Z: Integer 降噪次数
# 输出
#  0：降噪成功
#  1：降噪失败


# def clearNoise(image, G, N, Z):
#     draw = ImageDraw.Draw(image)

#     for i in xrange(0, Z):
#         for x in xrange(1, image.size[0] - 1):
#             for y in xrange(1, image.size[1] - 1):
#                 color = getPixel(image, x, y, G, N)
#                 if color != None:
#                     draw.point((x, y), color)

# # 测试代码


# def main():
#     # 打开图片
#     # image = Image.open("veriCode2.jpg")
#     image = Image.open(im)

#     # 将图片转换成灰度图片
#     image = image.convert("L")

#     # 去噪,G = 50,N = 4,Z = 4
#     clearNoise(image, 50, 4, 4)

#     # 保存图片
#     image.save("d:/result.jpg")


# if __name__ == '__main__':
#     main()

# a = 1
# t = False
# if not t and a == 1:
#     t = True
#     print '1st if', t
# if not t and a == 1:
#     print '2nd if', t
# elif t:
#     print '3rd if', t
# elif a == 1:
#     print '4th if', t
# else:
#     print 'last if', t

# try:
#     import cPickle as pickle
# except ImportError:
#     import pickle


# import os
# def getFileStr(level):
#     return '  '*level+'- '
# def getDicStr(level):
#     return '  '*level+'+'

# def printFile(path,level):
#     if os.path.exists(path):
#         files = os.listdir(path)
#         for f in files :
#             subpath=os.path.join(path,f)
#            #print(os.path.isfile(subpath))
#             if os.path.isfile(subpath):
#                 print(getFileStr(level)+os.path.basename(subpath))
#             else:
#                 leveli=level+1
#                 print(getDicStr(level)+os.path.basename(subpath))
#                 printFile(subpath,leveli)

# if __name__=='__main__':
#     printFile(r'D://SVN//IT//Source Code',1)

# import os


# def printFile(path, level):
#     if os.path.exists(path):
#         files = os.listdir(path)
#         for f in files:
#             subpath = os.path.join(path, f)
#             if os.path.isfile(subpath):
#                 print ' ' * level + '- ' + os.path.basename(subpath)
#             else:
#                 leveli = level + 1
#                 print ' ' * level + '- ' + os.path.basename(subpath)
#                 printFile(subpath, leveli)
# if __name__ == '__main__':
#     printFile(r'C:', 1)

# def _compute_login_user(n):
#     if n % 2 == 0:
#         login_user = True
#     else:
#         login_user = False
#     return login_user

# def _compute_login_user(n):
#     login_user = False
#     if n % 2 == 0:
#         login_user = True
#     return login_user

# def test():
#     for i in xrange(10000000):
#         _compute_login_user(i)

# if __name__ == '__main__':
#     import cProfile
#     cProfile.run("test()")

# import unittest

# def fun(x):
#     return x + 1

# class MyTest(unittest.TestCase):
#     def test(self):
#         self.assertEqual(fun(3), 5)

# def find_pair(A, target):
#     B = {}
#     for i in range(0, len(A)):
#         if A[i] <= target:
#             if not B.has_key(A[i]):
#                 B[A[i]] = [i]
#             else:
#                 B[A[i]].append(i)
#     for i in range(0, target / 2 + 1):
#         if B.has_key(i) and B.has_key(target-i):
#             print(i, B[i], target-i, B[target-i])

# if __name__ == "__main__":
#     A = [0, 1, 1, 2, 11, 8, 3, 4, 5, 6, 7, 8, 9, 10]
#     find_pair(A, 9)

# def find_pair(A, target):
#     A.sort()
#     i, j = 0, len(A) - 1
#     while i < j:
#         s = A[i] + A[j]
#         if s == target:
#             print(i, A[i], j, A[j])
#             i += 1
#             j -= 1
#         elif s < target:
#             i += 1
#         else:
#             j -= 1

# if __name__ == "__main__":
#     A = [0, 1, 1, 2, 11, 8, 3, 4, 5, 6, 7, 8, 9, 10]
#     find_pair(A, 9)

# import itertools as it, glob, os

# def multiple_file_types(*patterns):
#     return it.chain.from_iterable(glob.glob(pattern) for pattern in patterns)

# for filename in multiple_file_types("*.txt", "*.py"): # add as many filetype arguements
#     realpath = os.path.realpath(filename)
#     print realpath

# import json

# variable = ['hello', 42, [1,'two'],'apple']
# print "Original {0} - {1}".format(variable,type(variable))

# # encoding
# encode = json.dumps(variable)
# print "Encoded {0} - {1}".format(encode,type(encode))

# #deccoding
# decoded = json.loads(encode)
# print "Decoded {0} - {1}".format(decoded,type(decoded))
# import inspect

# def add(x, y=1):
#     f = inspect.currentframe()
#     print f.f_locals
#     print f.f_back
#     return x + y
# print add(2)

# import zlib

# string =  """   Lorem ipsum dolor sit amet, consectetu
#                 adipiscing elit. Nunc ut elit id mi ultricies
#                 adipiscing. Nulla facilisi. Praesent pulvinar,
#                 sapien vel feugiat vestibulum, nulla dui pretium orci,
#                 non ultricies elit lacus quis ante. Lorem ipsum dolor
#                 sit amet, consectetur adipiscing elit. Aliquam
#                 pretium ullamcorper urna quis iaculis. Etiam ac massa
#                 sed turpis tempor luctus. Curabitur sed nibh eu elit
#                 mollis congue. Praesent ipsum diam, consectetur vitae
#                 ornare a, aliquam a nunc. In id magna pellentesque
#                 tellus posuere adipiscing. Sed non mi metus, at lacinia
#                 augue. Sed magna nisi, ornare in mollis in, mollis
#                 sed nunc. Etiam at justo in leo congue mollis.
#                 Nullam in neque eget metus hendrerit scelerisque
#                 eu non enim. Ut malesuada lacus eu nulla bibendum
#                 id euismod urna sodales. """

# print "Original Size: {0}".format(len(string))

# compressed = zlib.compress(string)
# print "Compressed Size: {0}".format(len(compressed))

# decompressed = zlib.decompress(compressed)
# print "Decompressed Size: {0}".format(len(decompressed))


# import requests
# import json
# url = 'http://121.43.62.168/messagecenter/api/20150927/system/messagecenter/send'
# mobile = '18994600676'
# args = {"channel": 102, "targets": json.dumps([mobile]), 'topic': 'test', 'content': 'tyudfwewdfd'}
# respon = requests.post(url, data=args)
# r = json.loads(respon.text)
# print r

# import requests
# from requests.auth import HTTPBasicAuth
# import json
# url = 'https://github.com/'
# respon = requests.get(url, auth=HTTPBasicAuth('CharlesBird', '5377343zhon'))
# print respon.status_code

# import unittest
#
#
# class TestStringMethods(unittest.TestCase):
#
#     def setUp(self):
#         print 'init by setUp...'
#
#     def tearDown(self):
#         print 'end by tearDown...'
#
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
#         self.assertTrue('Foo'.isupper())
#
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)
#
#
# if __name__ == '__main__':
#     # unittest.main()
#     # 装载测试用例
#     test_cases = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
#     # 使用测试套件并打包测试用例
#     test_suit = unittest.TestSuite()
#     test_suit.addTests(test_cases)
#     # 运行测试套件，并返回测试结果
#     test_result = unittest.TextTestRunner(verbosity=2).run(test_suit)
#     #生成测试报告
#     print("testsRun:%s" % test_result.testsRun)
#     print("failures:%s" % len(test_result.failures))
#     print("errors:%s" % len(test_result.errors))
#     print("skipped:%s" % len(test_result.skipped))

# a = [0, [1, 2], 3]
# b = a[:]
# a[0] = 8
# a[1][1] = 9
# print a, b
#
# import copy
# a = [0, [1, 2], 3]
# b = copy.deepcopy(a)
# a[0] = 8
# a[1][1] = 9
# print a, b

# def test():
#     a = False
#     exec ("a = True")
#     print ("a = ", a)
# test()
#
# b = False
# exec ("b = True")
# print ("b = ", b)

# a = 'xianglong.me'
# print id(a)
# a = '1saying.com'
# print id(a)
# a_list = [1, 2, 3]
# print id(a_list)
# a_list.append(4)
# print id(a_list)

# def func_int(a):
#     a += 4
#
# def func_list(a_list=[]):
#     a_list[0] = 4
#
# t = 0
# func_int(t)
# print t
#
# t_list = [1, 2, 3]
# func_list(t_list)
# print t_list

# d = {'a':1}
# def f():
#     d = {}
#     d['b'] = 2
# f()
# print d

# # 协程
# import time
# import sys
# # 生产者


# def produce(l):
#     i = 0
#     while 1:
#         if i < 10:
#             l.append(i)
#             yield i
#             i = i + 1
#             time.sleep(0.5)
#         else:
#             return

# # 消费者


# def consume(l):
#     p = produce(l)
#     while 1:
#         try:
#             p.next()
#             while len(l) > 0:
#                 print l.pop()
#         except StopIteration:
#             sys.exit(0)
# l = []
# consume(l)


# import greenlet


# def fun1():
#     print("12")
#     gr2.switch()
#     print("56")
#     gr2.switch()


# def fun2():
#     print("34")
#     gr1.switch()
#     print("78")


# gr1 = greenlet.greenlet(fun1)
# gr2 = greenlet.greenlet(fun2)
# gr1.switch()


# import gevent


# def fun1():
#     print("www.baidu.com")   # 第一步
#     gevent.sleep(0)
#     print("end the baidu.com")  # 第三步


# def fun2():
#     print("www.zhihu.com")   # 第二步
#     gevent.sleep(0)
#     print("end th zhihu.com")  # 第四步

# gevent.joinall([
#     gevent.spawn(fun1),
#     gevent.spawn(fun2),
# ])


# import gevent
# import requests


# def func(url):
#     print("get: %s" % url)
#     gevent.sleep(0)
#     date = requests.get(url)
#     ret = date.text
#     print(url, len(ret))
# gevent.joinall([
#     gevent.spawn(func, 'https://www.baidu.com/'),
#     gevent.spawn(func, 'https://www.yahoo.com/'),
#     gevent.spawn(func, 'https://github.com/'),
# ])

# def gen():
#     while True:
#         s = yield 3
#         print s
# g = gen()
# g.next()
# g.send('234')

# def foo():
#     for i in range(5):
#         yield (i, '123')

# def f():
#     for k, v in foo():
#         print k, v
# f()


# from werkzeug.serving import run_simple
# from werkzeug.contrib.sessions import Session
# print type(Session)

import xmlrpclib
# url, db, username, password = 'http://192.168.3.49:8066', 'zhc_0228', 'support@unovo.com.cn', 'unovo883&'
url, db, username, password = 'http://192.168.3.51:8069', 'db-lianyuplus', 'support@unovo.com.cn', 'ahong883&'
# url, db, username, password = 'https://erp.unovo.com.cn:8443', 'db-lianyuplus', 'support@unovo.com.cn', 'ahong883&'
# url, db, username, password = 'http://192.168.3.51:8069', 'db-unovo', 'support@unovo.com.cn', 'ahong883&'
# url, db, username, password = 'http://192.168.3.51:8069', 'db-zhihui', 'support@unovo.com.cn', 'unovo883&'
# url, db, username, password = 'http://121.43.181.104:8069', 'linyan_dev', 'admin', 'admin'
common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})
models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url), allow_none=True)
models.execute_kw(db, uid, password, 'unovo.works', 'create_next_works', ["days"])
# models.execute_kw(db, uid, password, 'unovo.works', 'create_next_works', ["weeks"])
# employee = models.execute_kw(db, uid, password, 'hr.employee', 'search_read', [[], ['user_id']])
# for em in employee:
#     user_id = em['user_id'][0]
#     employee_id = em['id']
#     users = models.execute_kw(db, uid, password, 'res.users', 'search_read', [[('id', '=', user_id)], ['partner_id']])
#     partner_id = users[0]['partner_id'][0]
#     models.execute_kw(db, uid, password, 'hr.employee', 'write', [[employee_id], {'address_home_id': partner_id}])
# models.execute_kw(db, uid, password, 'stock.move', 'write', [[3614], {'reserved_quant_ids': [(6, 0, [])]}])
# contract_line = models.execute_kw(db, uid, password, 'linyan.contract.line', 'search_read', [[]])
# for line in contract_line:
#     sale_id, buy_id, relation_qty = line['contract_id'][0], line['buy_id'][0], line['actual_qty']
#     models.execute_kw(db, uid, password, 'linyan.sale.contract.line', 'create', [{'contract_id': buy_id, 'sale_id': sale_id, 'relation_qty': relation_qty}])
# fields = models.execute_kw(db, uid, password, 'res.partner', 'fields_get', [[]])
# for f in fields:
#     print f, fields[f]['type']
#     if fields[f]['type'] == 'many2one':
#         print fields[f]['relation']
# print models.execute_kw(db, uid, password, 'unovo.base.synchro', 'top_rpc_syn', [{'test': {'1': 1}}])
# print models.execute_kw(db, uid, password, 'res.partner', 'name_search', ['上海安理创科技有限公司', []])
# print models.execute_kw(db, uid, password, 'unovo.interface', 'erp_open_common_fnct', [{'method': 'supplier_partner_validate', 'value': {'ref': 'S00000012'}}])
# print models.execute_kw(db, uid, password, 'unovo.interface', 'erp_open_common_fnct', [{'method': 'supplier_partner_list_get', 'value': {'is_company': True, 'supplier': True, 'page_no': 0, 'page_size': 80}}])
# print models.execute_kw(db, uid, password, 'unovo.interface', 'erp_open_common_fnct', [{'method': 'supplier_partner_list_get', 'value': {'is_company': False, 'parent_id': 'S00000012'}}])
# print models.execute_kw(db, uid, password, 'unovo.interface', 'erp_open_common_fnct', [{'method': 'supplier_partner_form_get', 'value': {'is_company': True, 'supplier': True, 'ref': 'S00000012'}}])
# print models.execute_kw(db, uid, password, 'unovo.interface', 'erp_open_common_fnct', [{'method': 'supplier_partner_update', 'value': {'is_company': True, 'supplier': True, 'ref': 'S00000012', 'name': u'上海安理创科技有限公司'}}])
# print models.execute_kw(db, uid, password, 'unovo.interface', 'erp_open_common_fnct', [{'method': 'supplier_quote_list_get', 'value': {'partner_id': 'S00000073', 'state': 'done', 'page_no': 0, 'page_size': 80}}])
# print models.execute_kw(db, uid, password, 'unovo.interface', 'erp_open_common_fnct', [{'method': 'supplier_quote_form_get', 'value': {'partner_id': 'S00000073', 'inquiry_id': 'AO2017040070', 'product_id': 'H0202008111'}}])
# print models.execute_kw(db, uid, password, 'unovo.interface', 'erp_open_common_fnct', [{'method': 'supplier_quote_update', 'value': {'partner_id': 'S00000073', 'inquiry_id': 'AO2017040072', 'product_id': 'H0202008111', 'state': 'draft', 'price': 1.2, 'spq': 3000, 'l_t': 3}}])
# change_res = models.execute_kw(db, uid, password, 'unovo.interface', 'erp_open_common_fnct', [{
#     'method': 'supplier_quotechange_update',
#     'value': {
#         'name': '更换物料',
#         'product_mfg_pn': '品牌型号',
#         'product_mfg_name': '品牌',
#         'product_descript': '规格描述',
#         'partner_id': 'S00000034',
#         'inquiry_id': 'AO2017050099',
#         'product_id': 'H0101059012',
#         'price': 1.5,
#         'spq': 3000,
#         'l_t': 3,
#         'reason': 'eol'}
#     }])
# if change_res['valid']:
#     models.execute_kw(db, uid, password, 'unovo.interface', 'erp_open_common_fnct', [{
#         'method': 'supplier_quote_update',
#         'value': {
#             'partner_id': 'S00000034',
#             'inquiry_id': 'AO2017050099',
#             'product_id': 'H0101059012',
#             'reason': 'eol'}
#     }])
# print models.execute_kw(db, uid, password, 'unovo.interface', 'erp_open_common_fnct', [{'method': 'supplier_quotechange_form_get', 'value': {'partner_id': 'S00000073', 'inquiry_id': 'AO2017050102', 'product_id': 'H0202008111'}}])
# print models.execute_kw(db, uid, password, 'unovo.interface', 'erp_open_common_fnct', [{'method': 'mobile_groups_list_get', 'value': {'page_no': 0, 'page_size': 80}}])
# print models.execute_kw(db, uid, password, 'unovo.interface', 'erp_open_common_fnct', [{'method': 'mobile_users_list_get', 'value': {'page_no': 0, 'page_size': 80}}])
# print models.execute_kw(db, uid, password, 'unovo.interface', 'erp_open_common_fnct', [{'method': 'mobile_department_list_get', 'value': {'page_no': 0, 'page_size': 80}}])
# print models.execute_kw(db, uid, password, 'unovo.interface', 'erp_open_common_fnct', [{'method': 'mobile_employee_list_get', 'value': {'page_no': 0, 'page_size': 80}}])
# print models.execute_kw(db, uid, password, 'unovo.interface', 'erp_open_common_fnct', [{'method': 'mobile_department_list_get', 'value': {}}])
# print models.execute_kw(db, uid, password, 'unovo.interface', 'erp_open_common_fnct', [{'method': 'mobile_modulecategory_list_get', 'value': {}}])
# print models.execute_kw(db, uid, password, 'unovo.interface', 'erp_open_common_fnct', [{'method': 'mobile_partner_dropdown_list_get', 'value': {'is_company': True, 'customer': True, 'input': u''}}])
# print models.execute_kw(db, uid, password, 'unovo.interface', 'erp_open_common_fnct', [{
#     'method': 'mobile_project_update',
#     'value': {
#         'name': u'接口项目',
#         'user_id': 'jiangguoxiang@unovo.com.cn',
#         'partner_id': 'C00000040',
#         'unovo_operator_id': 'C00000040',
#         'project_type': 1,
#         'project_nature': 1,
#         'sale_type': 'normal',
#         'project_contact': u'蒋国翔',
#         'phone_number': '12123234242',
#         'project_address': '上海',
#         'state_id': 61,
#         'city': '上海',
#         'privacy_visibility': 'public',
#         'priority': '1',
#         'date_start': '2017-07-05',
#         'work_date': '2017-07-05',
#         'date': '2017-07-05',
#         'over_date': '2017-07-05',
#         'description': '备注'}
#     }])
# print models.execute_kw(db, uid, password, 'unovo.interface', 'erp_open_common_fnct', [{'method': 'mobile_countrystate_dropdown_list_get', 'value': {'input': ''}}])
# models.execute_kw(db, uid, password, 'unovo.logs', 'create', [{'res_type': 'unovo.repair', 'res_id': 91, 'status': 'approving', 'code': 'L-RO2018030001', 'type': 'approve', 'name': u'返修单', 'last_time': '2018-03-18 16:30:39', 'users': [(6, 0, [69])]}])
# models.execute_kw(db, uid, password, 'purchase.order.line', 'write', [[710, 711, 1041], {'taxes_id': [(6, 0, [8])]}])

# import odoorpc
# db = 'zhc_unovo'
# user = 'support@unovo.com.cn'
# passwd = 'unovo883&'
# odoo = odoorpc.ODOO('192.168.3.49', port='8066')
# odoo.login(db, user, passwd)
# partner = odoo.env['res.partner'].search([])
# print partner

# import jsonrpclib
# url, db, username, password = 'http://192.168.3.49:8066', 'zhc_unovo', 'support@unovo.com.cn', 'unovo883&'
# server = jsonrpclib.Server('{}/jsonrpc/common'.format(url))
# uid = server.authenticate(db, username, password, {})
# print uid

# res = {'partner': []}
# for partner in range(10):
#     res['partner'].append(partner)
# print res


# from pythonds.trees.binheap import BinHeap
# bh = BinHeap()
# bh.insert(5)
# bh.insert(7)
# bh.insert(3)
# bh.insert(11)
# print bh.delMin()
# print bh.delMin()

# class BinaryTree:

#     def __init__(self, rootObj):
#         self.key = rootObj
#         self.leftChild = None
#         self.rightChild = None

#     def insertLeft(self, newNode):
#         if self.leftChild == None:
#             self.leftChild = BinaryTree(newNode)
#         else:
#             t = BinaryTree(newNode)
#             t.leftChild = self.leftChild
#             self.leftChild = t

#     def insertRight(self, newNode):
#         if self.rightChild == None:
#             self.rightChild = BinaryTree(newNode)
#         else:
#             t = BinaryTree(newNode)
#             t.rightChild = self.rightChild
#             self.rightChild = t

#     def getRightChild(self):
#         return self.rightChild

#     def getLeftChild(self):
#         return self.leftChild

#     def setRootVal(self, obj):
#         self.key = obj

#     def getRootVal(self):
#         return self.key

# r = BinaryTree('a')
# print(r.getRootVal())
# print(r.getLeftChild())
# r.insertLeft('b')
# print(r.getLeftChild())
# print(r.getLeftChild().getRootVal())
# r.insertRight('c')
# print(r.getRightChild())
# print(r.getRightChild().getRootVal())
# r.getRightChild().setRootVal('hello')
# print(r.getRightChild().getRootVal())

# from Queue import Queue, Empty
# from threading import *
#
#
# class EventManager(object):
#
#     def __init__(self):
#         self.__eventQueue = Queue()  # 事件对象列表
#         self.__active = False  # 事件管理器开关
#         self.__thread = Thread(target=self.__Run)  # 事件处理线程
#         self.__handlers = {}  # 保存事件的响应函数，一对多
#
#     def __Run(self):
#         """运行引擎"""
#         while self.__active:
#             try:
#                 event = self.__eventQueue.get(
#                     block=True, timeout=1)  # 获取事件的阻塞时间为1秒
#                 self.__EventProcess(event)
#             except Empty:
#                 pass
#
#     def __EventProcess(self, event):
#         """处理事件"""
#         # 检查是否存在对该事件进行监听的处理函数
#         if event.type_ in self.__handlers:
#             # 若存在则将事件按顺序传递给处理函数
#             for handler in self.__handlers[event.type_]:
#                 handler(event)
#
#     def Start(self):
#         """启动"""
#         self.__active = True
#         # 启动事件处理线程
#         self.__thread.start()
#
#     def Stop(self):
#         """停止"""
#         self.__active = False
#         # 等待处理事件线程退出
#         self.__thread.join()
#
#     def AddEventListener(self, type_, handler):
#         """绑定事件和监听器处理函数"""
#         try:
#             handlerList = self.__handlers[type_]  # 获取事件类型对应处理函数列表，无则创建
#         except KeyError:
#             handlerList = []
#         self.__handlers[type_] = handlerList
#         if handler not in handlerList:
#             handlerList.append(handler)  # 处理函数不在该事件处理列表中，则注册该事件
#
#     def RemoveEventListner(self, type_, handler):
#         self.__handlers[type_].move(handler)
#
#     def sentEvent(self, event):
#         """发送事件，向事件列表中存入事件"""
#         self.__eventQueue.put(event)
#
#
# """事件对象"""
#
#
# class Event(object):
#
#     def __init__(self, type_):
#         self.type_ = type_
#         self.dict = {}
#
#
# from datetime import datetime
#
# """事件名称"""
# EVENT_ARTICAL = "Event_Article"
#
#
# class PublicAccounts(object):
#
#     def __init__(self, eventManager):
#         self.__eventManager = eventManager
#
#     def WriteNewArtical(self):
#         event = Event(EVENT_ARTICAL)
#         event.dict['artical'] = u"如何写出更优雅的文章\n"
#         self.__eventManager.sentEvent(event)
#         print u'公众号发布新文章\n'
#
#
# class Listener(object):
#
#     def __init__(self, username):
#         self.__username = username
#
#     def ReadArtical(self, event):
#         print u'%s 收到新文章' % self.__username
#         print u'正在阅读新文章内容： %s' % event.dict['artical']
#
#
# def test():
#     listner1 = Listener("thinkroom")  # 订阅者1
#     listner2 = Listener("steve")  # 订阅者2
#
#     eventManager = EventManager()
#
#     # 绑定事件和监听器响应函数(新文章)
#     eventManager.AddEventListener(EVENT_ARTICAL, listner1.ReadArtical)
#     eventManager.AddEventListener(EVENT_ARTICAL, listner2.ReadArtical)
#     eventManager.Start()
#
#     publicAcc = PublicAccounts(eventManager)
#     timer = Timer(2, publicAcc.WriteNewArtical)
#     timer.start()
#
# if __name__ == '__main__':
#     test()


# def line_splitter(delimiter=None):
#     print("Ready to split")
#     result = '123456'
#     while True:
#         line = (yield result)
#         result = line.split(delimiter)

# s = line_splitter(',')
# print s.next()
# print s.send('1,2,3')
# print s.send('a,b,c')

# data = {1: ['a'], 2: [], 3: [], 4: []}

# def foo(old_value, node_id, l=[]):
#     for node in old_value:
#         if node_id == node['parent_id']:
#             child_id = node['id']
#             for node2 in old_value:
#                 if child_id


# log_value = {'tp': 'tp', 'server_db': 'server_db', 'user_id': 'user_id', 'server_id': 'server', 'model_name': 'model', 'remote_id': 'remote_id'}
# args = 'remote_id', 'test', {'tp': 'tp', 'server_db': 'server_db', 'user_id': 'user_id', 'server_id': 'server', 'model_name': 'model', 'remote_id': 'remote_id'}

# def foo1(a, b, c):
#     print a, b, c

# foo1(*args)

# import threading
# from werkzeug.local import Local
# l = Local()
# l.__storage__
# def add_arg(arg, i):
#     l.__setattr__(arg, i)
# for i in range(3):
#     arg = 'arg' + str(i)
#     t = threading.Thread(target=add_arg, args=(arg, i))
#     t.start()
# print l.__storage__
# print l.__ident_func__

# from werkzeug.local import Local, LocalManager, release_local, LocalStack
# loc = Local()
# loc.foo = 42
# release_local(loc)

# print hasattr(loc, 'foo')

# ls = LocalStack()
# request = ls()


# class WebRequest(object):
#     def __init__(self, httprequest):
#         self.httprequest = httprequest
#         self.name = None

#     def foo1(self):
#         return 'foo1'

#     @property
#     def foo2(self):
#         return 'foo2'

#     def __enter__(self):
#         print '1111111111'
#         ls.push(self)
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         print exc_type, exc_value, traceback
#         ls.pop()
# with WebRequest({"123": "2342"}) as wr:
#     wr.foo1()
#     print request.__dict__

# from werkzeug.wrappers import Request, Response
# from werkzeug.serving import run_simple

# def application(environ, start_response):
#     httprequest = Request(environ)
#     response = Response("Hello, %s" % httprequest.args.get('name', ''), headers={'123': 'sds'})
#     return response(environ, start_response)

# if __name__ == '__main__':
#     run_simple('localhost', 4000, application)

# def foo():
#     print "Part 1"
#     yield
#     print "Part 2"
#     yield
#
# f = foo()
# f.send(None)
# f.send(None)

# import redis
# pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
# r = redis.Redis(connection_pool=pool)
# r.set('hello', 'world')
# r.append('hello', 1)
# print r.get('hello')

# import matplotlib.pyplot as plt
# plt.xlabel(u'性别')
# plt.ylabel(u'人数')
# plt.xticks((0,1),(u'男',u'女'))
# plt.title(u"性别比例分析")
# rect = plt.bar(left = (0, 1),height = (1, 0.5), width=0.35, align="center")
# plt.legend((rect,),(u"图例",))
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# u = np.linspace(-1,1,100)
# x,y = np.meshgrid(u,u)     # 网格坐标生成函数
# z = np.abs((1-x**2-y**2))**0.5
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.plot_surface(x,y,z,rstride=4,cstride=4,cmap='rainbow')
# plt.show()

# import numpy as np
# import urllib
# from sklearn import metrics
# from sklearn.ensemble import ExtraTreesClassifier
# from sklearn import preprocessing
# url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
# raw_data = urllib.urlopen(url)
# dataset = np.loadtxt(raw_data, delimiter=",")
# X = dataset[:, 0:7]
# y = dataset[:, 8]
# model = ExtraTreesClassifier()
# model.fit(X, y)
# print model.feature_importances_

# import numpy as np
# import urllib
# from sklearn import metrics
# from sklearn.linear_model import LogisticRegression
# url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
# raw_data = urllib.urlopen(url)
# dataset = np.loadtxt(raw_data, delimiter=",")
# X = dataset[:, 0:7]
# y = dataset[:, 8]
# model = LogisticRegression()
# model.fit(X, y)
# print 'MODEL'
# print model
# expected = y
# predicted = model.predict(X)
# print('RESULT')
# print(metrics.classification_report(expected, predicted))
# print('CONFUSION MATRIX')
# print(metrics.confusion_matrix(expected, predicted))

# import numpy as np
# import urllib
# from sklearn import metrics
# # from sklearn.naive_bayes import GaussianNB
# # from sklearn.neighbors import KNeighborsClassifier
# # from sklearn.tree import DecisionTreeClassifier
# from sklearn.svm import SVC
# url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
# raw_data = urllib.urlopen(url)
# dataset = np.loadtxt(raw_data, delimiter=",")
# X = dataset[:, 0:7]
# y = dataset[:, 8]
# # model = GaussianNB()
# # model = KNeighborsClassifier()
# # model = DecisionTreeClassifier()
# model = SVC()
# model.fit(X, y)
# print('MODEL')
# print(model)
# expected = y
# predicted = model.predict(X)
# print('RESULT')
# print(metrics.classification_report(expected, predicted))
# print('CONFUSION MATRIX')
# print(metrics.confusion_matrix(expected, predicted))

# 最小二叉堆
# class BinHeap:
#     def __init__(self):
#         self.heapList = [0]
#         self.currentSize = 0
 
 
#     def percUp(self,i):
#         while i // 2 > 0:
#           if self.heapList[i] < self.heapList[i // 2]:
#              tmp = self.heapList[i // 2]
#              self.heapList[i // 2] = self.heapList[i]
#              self.heapList[i] = tmp
#           i = i // 2
 
#     def insert(self,k):
#       self.heapList.append(k)
#       self.currentSize = self.currentSize + 1
#       self.percUp(self.currentSize)
 
#     def percDown(self,i):
#       while (i * 2) <= self.currentSize:
#           mc = self.minChild(i)
#           if self.heapList[i] > self.heapList[mc]:
#               tmp = self.heapList[i]
#               self.heapList[i] = self.heapList[mc]
#               self.heapList[mc] = tmp
#           i = mc
 
#     def minChild(self,i):
#       if i * 2 + 1 > self.currentSize:
#           return i * 2
#       else:
#           if self.heapList[i*2] < self.heapList[i*2+1]:
#               return i * 2
#           else:
#               return i * 2 + 1
 
#     def delMin(self):
#       retval = self.heapList[1]
#       self.heapList[1] = self.heapList[self.currentSize]
#       self.currentSize = self.currentSize - 1
#       self.heapList.pop()
#       self.percDown(1)
#       return retval
 
#     def buildHeap(self,alist):
#       i = len(alist) // 2
#       self.currentSize = len(alist)
#       self.heapList = [0] + alist[:]
#       while (i > 0):
#           self.percDown(i)
#           i = i - 1
 
# bh = BinHeap()
# bh.buildHeap([9,5,6,2,3])
 
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())


# import qrcode 
# qr = qrcode.QRCode(     
#     version=1,     
#     error_correction=qrcode.constants.ERROR_CORRECT_L,     
#     box_size=10,     
#     border=4, 
# ) 
# qr.add_data('http://192.168.3.49:8066/web?debug=#id=1&view_type=form&model=hr.expense.expense&menu_id=738&action=936') 
# qr.make(fit=True)  
# img = qr.make_image()
# print type(img)
# img.save('D:/SVN/123.png')


# import datetime
# import time
# today = time.strftime('%Y-%m-%d')
# days = int(time.strftime('%w'))
# if days == 0:
#     days = 7
# start_date = datetime.datetime.strptime(today, '%Y-%m-%d')
# date1 = (start_date + datetime.timedelta(days=8-days)).strftime("%Y-%m-%d")
# date2 = (start_date + datetime.timedelta(days=14-days)).strftime("%Y-%m-%d")
# print date1, date2


# from barcode.writer import ImageWriter
# from barcode.codex import Code39
# from PIL import Image, ImageDraw, ImageFont, ImageWin
# from StringIO import StringIO


# def generagteBarCode(self):
#     imagewriter = ImageWriter()
#     #保存到图片中
#     # add_checksum : Boolean   Add the checksum to code or not (default: True)
#     ean = Code39("1234567890", writer=imagewriter, add_checksum=False)
#     # 不需要写后缀，ImageWriter初始化方法中默认self.format = 'PNG'
#     print '保存到image2.png'
#     ean.save('image2')
#     img = Image.open('image2.png')
#     print '展示image2.png'
#     img.show()

#     # 写入stringio流中
#     i = StringIO()
#     ean = Code39("0987654321", writer=imagewriter, add_checksum=False)
#     ean.write(i)
#     i = StringIO(i.getvalue())
#     img1 = Image.open(i)
#     print '保存到stringIO中并以图片方式打开'
#     img1.show()


# def consume():
#     a = 0
#     while True:
#         print('before yield a: %s' % a)
#         n = yield a
#         print('after yield n: %s, a: %s' %(n, a))
#         a = 'OK'
#         print(n, a)

# c = consume()
# c.next()
# r = c.send('1')
# print r
# c.send('a')
# c.send('b')