from traits.api import HasTraits, Str, Int, Array, List


class MetadataTest(HasTraits):
    i = Int(99, myinfo='test my info')
    s = Str('test', label='String')
    a = Array
    list = List(Int)


test = MetadataTest()
test.configure_traits()
