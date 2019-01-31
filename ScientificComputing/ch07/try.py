from traits.api import HasTraits, Int, Str
from traitsui.api import View, Item, Group
# View描述了界面的视图类，Item模块描述了界面中的控件类


class ModelManager(HasTraits):
    model_name = Str
    category = Str
    model_file = Str
    model_number = Int
    vertices = Int

    view1 = View(
        Group(
            Item("model_name", label='a'),
            Item("model_file", label='b'),
            Item("category", label='c'),
            label='d',
            show_border=True
        ),
        Group(
            Item("model_number", label='e'),
            Item("vertices", label='f'),
            label=u'g',
            show_border=True
        ),
    )


model = ModelManager()
model.configure_traits()
