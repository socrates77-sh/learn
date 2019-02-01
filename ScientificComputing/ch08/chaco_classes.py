# -*- coding: utf-8 -*-
from chaco.api import AbstractMapper, AbstractDataRange, AbstractDataSource


def subclasses(cls):
    print(cls)
    for c in cls.__subclasses__():
        subclasses(c)


subclasses(AbstractMapper)
print('\n')
subclasses(AbstractDataRange)
print('\n')
subclasses(AbstractDataSource)
