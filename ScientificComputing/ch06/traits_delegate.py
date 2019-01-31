from traits.api import *


class System(HasTraits):
    name = Str


class CPU(HasTraits):
    cpu_type = Str


class PC(HasTraits):
    os = Instance(System)
    cpu = Instance(CPU)

    cpu_type = DelegatesTo('cpu')
    os_name = DelegatesTo('os', prefix='name')

    def _os_name_changed(self):
        print('OS changed to ', self.os_name)
