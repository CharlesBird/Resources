"""修饰模式"""


class TextTag(object):

    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class BlodWrapper(TextTag):

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<b>{}</b>".format(self._wrapped.render())


class ItalicWrapper(TextTag):

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<i>{}<i>".format(self._wrapped.render())


if __name__ == '__main__':
    tg = TextTag("Hello world.")
    wra_tg = ItalicWrapper(BlodWrapper(TextTag("Hello world.")))

    print(tg.render())
    print(wra_tg.render())