"""桥接，实现接口层与实现分离"""


class DrawingAPI1(object):
    def draw_circle(self, x, y, radius):
        print('API1 circle at {}:{} radius {}'.format(x, y, radius))


class DrawingAPI2(object):
    def draw_circle(self, x, y, radius):
        print('API2 circle at {}:{} radius {}'.format(x, y, radius))


class CircleShape(object):

    def __init__(self, x, y, radius, drawing_api):
        self.x = x
        self.y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        self._drawing_api.draw_circle(self.x, self.y, self._radius)

    def scale(self, pct):
        self._radius *= pct


def main():
    shapes = (CircleShape(1, 2, 3, DrawingAPI1()), CircleShape(5, 6, 7, DrawingAPI2()))
    for shape in shapes:
        shape.scale(3)
        shape.draw()


if __name__ == '__main__':
    main()