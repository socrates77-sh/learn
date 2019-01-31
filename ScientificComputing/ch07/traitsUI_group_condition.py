from traits.api import HasTraits, Str, Int, Enum, Bool
from traitsui.api import View, Item, Group, VGroup, HGroup


class Shape(HasTraits):
    shape_type = Enum('rectangle', 'circle')
    editalbe = Bool

    x, y, w, h, r = [Int]*5

    view = View(
        VGroup(
            HGroup(Item('shape_type'), Item('editalbe')),
            VGroup(Item('x'), Item('y'), Item('w'), Item('h'),
                   visible_when="shape_type=='rectangle'",
                   enabled_when="editalbe"),
            VGroup(Item('x'), Item('y'), Item('r'),
                   visible_when="shape_type=='circle'",
                   enabled_when="editalbe"),
        ),
        resizable=True
    )


if __name__ == '__main__':
    p = Shape()
    p.configure_traits()
