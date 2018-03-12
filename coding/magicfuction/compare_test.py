"""比较操作符的使用"""
class CompareClass(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        print('lt')
        return self.age < other.age

    def __le__(self, other):
        print('le')
        return self.age <= other.age

    def __eq__(self, other):
        print('eq')
        return self.age == other.age

    def __ne__(self, other):
        print('ne')
        return self.age != other.age

    def __gt__(self, other):
        print('gt')
        return self.age > other.age

    def __ge__(self, other):
        print('ge')
        return self.age >= other.age

cc1 = CompareClass('Charles', 20)
cc2 = CompareClass('Charles', 30)
print('-----lt--------------')
print(cc1 < cc2)
print('-----le--------------')
print(cc1 <= cc2)
print('-----eq--------------')
print(cc1 == cc2)
print('-----ne--------------')
print(cc1 != cc2)
print('-----gt--------------')
print(cc1 > cc2)
print('-----gt--------------')
print(cc1 >= cc2)