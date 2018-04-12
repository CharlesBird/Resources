from unique_sequense import Singleton


class Test1(Singleton):

    def __init__(self, name, value):
        self.name = name
        self.value = value