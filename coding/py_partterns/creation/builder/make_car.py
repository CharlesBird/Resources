import abc


class CarModel(abc.ABC):

    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass

    @abc.abstractmethod
    def alarm(self):
        pass

    @abc.abstractmethod
    def enginBoom(self):
        pass

    def run(self):
        for action in self.sequence:
            if action == 'start':
                self.start()
            elif action == 'stop':
                self.stop()
            elif action == 'alarm':
                self.alarm()
            elif action == 'engine boom':
                self.enginBoom()

    def setSequence(self, sequence=None):
        self.sequence = sequence


class BMWModel(CarModel):

    def alarm(self):
        print("宝马车喇叭声音")

    def enginBoom(self):
        print("宝马车引擎")

    def start(self):
        print("宝马车跑起来")

    def stop(self):
        print("宝马车应该这样停车")


class BenZModel(CarModel):

    def alarm(self):
        print("奔驰车喇叭声音")

    def enginBoom(self):
        print("奔驰车引擎")

    def start(self):
        print("奔驰车跑起来")

    def stop(self):
        print("奔驰车应该这样停车")


class CarBuilder(abc.ABC):

    @abc.abstractmethod
    def getCarModel(self):
        pass


class BenZBuilder(CarBuilder):

    def __init__(self):
        self.car_model = BenZModel()

    def getCarModel(self):
        return self.car_model

    def setSequence(self, seq):
        self.car_model.setSequence(seq)


class BMWBuilder(CarBuilder):

    def __init__(self):
        self.car_model = BMWModel()

    def getCarModel(self):
        return self.car_model

    def setSequence(self, seq):
        self.car_model.setSequence(seq)



class Director(object):

    def __init__(self):
        self.benzBuilder = BenZBuilder()
        self.bmwBuilder = BMWBuilder()

    def getABenzModel(self):
        self.benzBuilder.setSequence(['start', 'engine boom', 'stop'])
        return self.benzBuilder.getCarModel()

    def getBBenzModel(self):
        self.benzBuilder.setSequence(['start', 'stop'])
        return self.benzBuilder.getCarModel()

    def getABMWModel(self):
        self.bmwBuilder.setSequence(['start', 'engine boom', 'stop'])
        return self.bmwBuilder.getCarModel()

    def getBBMWModel(self):
        self.bmwBuilder.setSequence(['start', 'stop', 'alarm'])
        return self.bmwBuilder.getCarModel()


if __name__ == '__main__':
    d = Director()
    d.getABenzModel().run()
    d.getBBenzModel().run()
    d.getABMWModel().run()
    d.getBBMWModel().run()