"""适配器，使得类接口兼容"""


class Dog(object):

    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "Woof"


class Cat(object):

    def __init__(self):
        self.name = "Cat"

    def meow(self):
        return "meow"


class Human(object):

    def __init__(self):
        self.name = "Human"

    def speek(self):
        return "Hello"


class Car(object):

    def __init__(self):
        self.name = "Car"

    def make_noise(self, n):
        return "vroom " * n


class Adapter(object):
    """适配器类，统一接口方法名称"""

    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

    def original_dict(self):
        return self.obj.__dict__


def main():
    objects = []
    dog = Dog()
    objects.append(Adapter(dog, make_noise=dog.bark))
    cat = Cat()
    objects.append(Adapter(cat, make_noise=cat.meow))
    human = Human()
    objects.append(Adapter(human, make_noise=human.speek))
    car = Car()
    objects.append(Adapter(car, make_noise=lambda: car.make_noise(5)))

    for o in objects:
        print("A {0} goes {1}".format(o.name, o.make_noise()))


if __name__ == '__main__':
    main()