from traits.api import *


class Point(HasTraits):
    x = Float(0.0)
    y = Float(0.0)
    updated = Event

    @on_trait_change('x,y')
    def pos_changed(self):
        self.updated = True

    def _updated_fired(self):
        self.redraw()

    def redraw(self):
        print('redraw at %s, %s' % (self.x, self.y))


if __name__ == '__main__':
    p = Point()
