"""状态模式"""


class State(object):

    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Scanning... Station is %s %s" % (self.stations[self.pos], self.name))


class AmState(State):

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = 'AM'

    def toggle_amfm(self):
        print("Switch to FM")
        self.radio.state = self.radio.fmstate


class FmState(State):

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = 'FM'

    def toggle_amfm(self):
        print("Switch to AM")
        self.radio.state = self.radio.amstate


class Radio(object):

    def __init__(self):
        self.amstate = AmState(self)
        self.fmstate = FmState(self)
        self.state = self.amstate

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()


if __name__ == '__main__':
    radio = Radio()
    actions = [radio.scan] * 2 + [radio.toggle_amfm] + [radio.scan] * 2
    actions *= 2
    for action in actions:
        action()