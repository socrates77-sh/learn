from traits.api import HasTraits, Str, Int, Instance, Delegate


class Parent(HasTraits):
    last_name = Str('Zhang')


class Child(HasTraits):
    age = Int
    father = Instance(Parent)
    last_name = Delegate('father')

    def _age_changed(self, old, new):
        print('Age changed from %s to %s' % (old, new))


Parent().configure_traits()
