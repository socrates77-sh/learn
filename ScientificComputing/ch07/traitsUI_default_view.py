from traits.api import *


class Employee(HasTraits):
    name = Str
    department = Str
    salary = Int
    bonus = Int


Employee().configure_traits()
