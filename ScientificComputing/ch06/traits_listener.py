from traits.api import HasTraits, Str, Int


class Child(HasTraits):
    name = Str
    age = Int
    doing = Str

    def __str__(self):
        return '%s<%x>' % (self.name, id(self))

    def _age_changed(self, old, new):
        print('%s.age changed: from %s to %s' % (self, old, new))

    def _anytrait_changed(self, name, old, new):
        print('anytrait changed: %s.%s frome %s to %s' %
              (self, name, old, new))


def log_trait_changed(obj, name, old, new):
    print('log: %s.%s changed frome %s to %s' %
          (obj, name, old, new))


if __name__ == '__main__':
    h = Child(name='HaiYue', age=4)
    k = Child(name='Kaiyu', age=1)
    h.on_trait_change(log_trait_changed, name='doing')
