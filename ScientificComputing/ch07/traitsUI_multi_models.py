from traits.api import HasTraits, Str, Int
from traitsui.api import View, Item, Group

comp_view = View(
    Group(
        Group(
            Item('p1.department', label='部门'),
            Item('p1.name', label='姓名'),
            Item('p1.salary', label='工资'),
            Item('p1.bonus', label='奖金'),
            show_border=True
        ),

        Group(
            Item('p2.department', label='部门'),
            Item('p2.name', label='姓名'),
            Item('p2.salary', label='工资'),
            Item('p2.bonus', label='奖金'),
            show_border=True
        ),
        orientation='horizontal'
    ),
    title='员工对比'
)


class Employee(HasTraits):
    name = Str
    department = Str
    salary = Int
    bonus = Int


if __name__ == '__main__':
    employee1 = Employee(department='开发', name='张三', salary=3000, bonus=300)
    employee2 = Employee(department='销售', name='李四', salary=4000, bonus=400)
    HasTraits().configure_traits(view=comp_view,
                                 context={'p1': employee1, 'p2': employee2})
