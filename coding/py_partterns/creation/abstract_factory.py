"""抽象工厂"""


class PetShop(object):
    def __init__(self, animal_factory):
        self.pet_factory = animal_factory

    def show_pet(self):
        pet = self.pet_factory()
        print("It's a lovely {}".format(pet))
        print("It says {}".format(pet.speek()))


class Dog(object):

    def speek(self):
        return "汪汪汪"

    def __str__(self):
        return "Dog"


class Cat(object):

    def speek(self):
        return "喵喵喵"

    def __str__(self):
        return "Cat"


if __name__ == '__main__':
    import random
    cat_pet = PetShop(Cat)
    cat_pet.show_pet()
    print("")
    for i in range(5):
        shop = PetShop(random.choice([Dog, Cat]))
        shop.show_pet()
        print("*" * 20)

