from traits.api import HasTraits, Str, Int
from traitsui.api import View, Item, Group

g1 = [Item('department', label='部门', tooltip='在哪个部门'),
      Item('name', label='姓名')]

g2 = [Item('salary', label='工资'),
      Item('bonus', label='奖金')]


class Employee(HasTraits):
    name = Str
    department = Str
    salary = Int
    bonus = Int

    traits_view = View(
        Group(*g1, label=u'个人信息', show_border=True),
        Group(*g2, label=u'收入', show_border=True),
        title='缺省内部视图'
    )

    another_view = View(
        Group(*g1, label=u'个人信息', show_border=True),
        Group(*g2, label=u'收入', show_border=True),
        title=u'另一个内部视图'
    )


global_view = View(
    Group(*g1, label=u'个人信息', show_border=True),
    Group(*g2, label=u'收入', show_border=True),
    title=u'外部视图'
)


if __name__ == '__main__':
    p = Employee()
    p.edit_traits()
    p.edit_traits(view='another_view')
    p.configure_traits(view=global_view)
