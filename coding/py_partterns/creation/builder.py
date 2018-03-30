"""建造者"""


class Director(object):

    def __init__(self):
        self.builder = None

    def construct_building(self):
        self.builder.new_building()
        self.builder.build_floor()
        self.builder.build_size()

    def get_build(self):
        return self.builder.building


class Building(object):

    def __init__(self):
        self.floor = None
        self.size = None

    def __str__(self):
        return 'Floor: %s | Size: %s' % (self.floor, self.size)


class Builder(object):

    def __init__(self):
        self.building = None

    def new_building(self):
        self.building = Building()

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError


class BuilderHouse(Builder):

    def build_floor(self):
        self.building.floor = '一个'

    def build_size(self):
        self.building.size = '大'


class BuilderFlag(Builder):

    def build_floor(self):
        self.building.floor = '很多个'

    def build_size(self):
        self.building.size = '小'


if __name__ == '__main__':
    d = Director()
    d.builder = BuilderHouse()
    d.construct_building()
    building = d.get_build()
    print('House: ', building)
    d = Director()
    d.builder = BuilderFlag()
    d.construct_building()
    building = d.get_build()
    print('Flag: ', building)