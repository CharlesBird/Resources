"""解释器模式"""


class Context(object):
    def __init__(self):
        self.input = ""
        self.output = ""


class AbstractExpression(object):

    def interpret(self, context):
        pass


class Expression(AbstractExpression):
    def interpret(self, context):
        print("Terminal interpret")


class NonterminalExpression(AbstractExpression):
    def interpret(self, context):
        print("Nonterminal interpret")


if __name__ == '__main__':
    context = ""
    c = []
    c = c + [Expression()]
    c = c + [NonterminalExpression()]
    c = c + [Expression()]
    c = c + [Expression()]
    for a in c:
        a.interpret(context)