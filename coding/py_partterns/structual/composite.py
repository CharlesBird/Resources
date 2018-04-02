"""组合模式，部分-整体，tree结构的表现"""


class Graphic(object):

    def render(self):
        raise NotImplementedError("继承类。")


class CompositeGraphic(Graphic):

    def __init__(self):
        self.graphics = []

    def render(self):
        for graphic in self.graphics:
            graphic.render()

    def add(self, graphic):
        self.graphics.append(graphic)

    def remove(self, graphic):
        self.graphics.remove(graphic)


class Ellipse(Graphic):

    def __init__(self, name):
        self.name = name

    def render(self):
        print("Ellipse: {}".format(self.name))


if __name__ == '__main__':
    e1 = Ellipse("a")
    e2 = Ellipse("b")
    e3 = Ellipse("c")
    e4 = Ellipse("d")
    e5 = Ellipse("e")

    g1 = CompositeGraphic()
    g2 = CompositeGraphic()

    g1.add(e1)
    g1.add(e2)
    g1.add(e3)
    g2.add(e4)
    g2.add(e5)

    g = CompositeGraphic()
    g.add(g1)
    g.add(g2)

    g.render()