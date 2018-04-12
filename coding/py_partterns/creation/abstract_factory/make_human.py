class YellowHuman(object):

    def getColor(self):
        print("黄色皮肤")

    def talk(self):
        print("黄种人说双字节")


class BlackHuman(object):

    def getColor(self):
        print("黑色皮肤")

    def talk(self):
        print("黑种人说话，一般人听不懂")


class WhiteHuman(object):

    def getColor(self):
        print("白色皮肤")

    def talk(self):
        print("白种人说单字节")


class HumanFactory(object):
    def __init__(self, sex_factory):
        self.sex_faxtory = sex_factory

    def createHuman(self, human='yellow'):
        humans = dict(yellow=YellowHuman, black=BlackHuman, white=WhiteHuman)
        return humans[human]()


class FemaleYellowHuman(YellowHuman):
    def getSex(self):
        print("黄人女性")


class MaleYellowHuman(YellowHuman):
    def getSex(self):
        print("黄人男性")


class FemaleBlackHuman(BlackHuman):
    def getSex(self):
        print("黑人女性")


class MaleBlackHuman(BlackHuman):
    def getSex(self):
        print("黑人男性")


class FemaleWhiteHuman(WhiteHuman):
    def getSex(self):
        print("白人女性")


class MaleWhiteHuman(WhiteHuman):
    def getSex(self):
        print("白人男性")


class FemaleFactory(object):

    def createYellowHuman(self):
        return FemaleYellowHuman()

    def createBlackHuman(self):
        return FemaleBlackHuman()

    def createWhiteHuman(self):
        return FemaleWhiteHuman()


class MaleFactory(object):

    def createYellowHuman(self):
        return MaleYellowHuman()

    def createBlackHuman(self):
        return MaleBlackHuman()

    def createWhiteHuman(self):
        return MaleWhiteHuman()


if __name__ == '__main__':
    femaleFactory = FemaleFactory()
    yellowHuman = femaleFactory.createYellowHuman()
    yellowHuman.getColor()
    yellowHuman.talk()
    yellowHuman.getSex()