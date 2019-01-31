from traits.api import HasTraits, Str, Int
from traitsui.api import View, Item, Group, Handler
from traitsui.menu import ModalButtons


g1 = [Item('department', label='部门', tooltip='在哪个部门'),
      Item('name', label='姓名')]

g2 = [Item('salary', label='工资'),
      Item('bonus', label='奖金')]


class Employee(HasTraits):
    name = Str
    department = Str
    salary = Int
    bonus = Int

    def _department_changed(self):
        print(self, 'department changed to ', self.department)

    def __str__(self):
        return '<Employee at 0x%xx>' % id(self)


view1 = View(
    Group(*g1, label=u'个人信息', show_border=True),
    Group(*g2, label=u'收入', show_border=True),
    title=u'外部视图',
    kind='modal',
    buttons=ModalButtons)


class EmployeeHandler(Handler):
    def init(self, info):
        super(EmployeeHandler, self).init(info)
        print('init called')

    def init_info(self, info):
        super(EmployeeHandler, self).init_info(info)
        print('init info called')

    def position(self, info):
        super(EmployeeHandler, self).position(info)
        print('position called')

    def setattr(self, info, obj, name, value):
        super(EmployeeHandler, self).setattr(info, obj, name, value)
        print('setattr called: %s.%s=%s' % (obj, name, value))

    def apply(self, info):
        super(EmployeeHandler, self).apply(info)
        print('apply called')

    def close(self, info, is_ok):
        super(EmployeeHandler, self).close(info, is_ok)
        print('close called: %s' % is_ok)
        return True

    def closed(self, info, is_ok):
        super(EmployeeHandler, self).closed(info, is_ok)
        print('closed called: %s' % is_ok)

    def revert(self, info):
        super(EmployeeHandler, self).revert(info)
        revert('apply called')


if __name__ == '__main__':
    zhang = Employee(name='Zhang')
    print('zhang is ', zhang)
    zhang.configure_traits(view=view1, handler=EmployeeHandler())
