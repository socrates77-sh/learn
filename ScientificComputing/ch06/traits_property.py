from traits.api import HasTraits, Float, Property, cached_property


class Rectangle(HasTraits):
    width = Float(1.0)
    height = Float(2.0)
    area = Property(depends_on=['width', 'height'])

    @cached_property
    def _get_area(self):
        print('recalculating')
        return self.width*self.height


r = Rectangle()
r.configure_traits()
# r.edit_traits()
