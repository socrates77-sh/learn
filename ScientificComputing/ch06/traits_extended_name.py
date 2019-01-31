from traits.api import *


class HasName(HasTraits):
    name = Str()

    def __str__(self):
        return '<%s %s>' % (self.__class__.__name__, self.name)


class Inner(HasName):
    x = Int
    y = Int


class Demo(HasName):
    x = Int
    y = Int
    z = Int(monitor=1)
    inner = Instance(Inner)
    alist = List(Int)
    test1 = Str()
    test2 = Str()

    def __inner_default(self):
        return Inner(name='inner1')

    @on_trait_change('x,y,inner.[x,y], test+, +monitor, alist[]')
    def event(self, obj, name, old, new):
        print(obj, name, old, new)


if __name__ == '__main__':
    d = Demo(name='demo')
