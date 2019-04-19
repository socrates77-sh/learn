import unittest

import numpy as np
from sort_algorithm import *


class MyTest_Instersion_Sort(unittest.TestCase):
    def test_int_list(self):
        l = list(np.random.randint(1000, size=1000))
        my_sort = instersion_sort(l)
        golden_sort = sorted(l)
        self.assertEqual(my_sort, golden_sort)

    def test_float_list(self):
        l = list(np.random.random(size=1000))
        my_sort = instersion_sort(l)
        golden_sort = sorted(l)
        self.assertEqual(my_sort, golden_sort)


class MyTest_Selection_Sort(unittest.TestCase):
    def test_int_list(self):
        l = list(np.random.randint(1000, size=1000))
        my_sort = selection_sort(l)
        golden_sort = sorted(l)
        self.assertEqual(my_sort, golden_sort)

    def test_float_list(self):
        l = list(np.random.random(size=1000))
        my_sort = selection_sort(l)
        golden_sort = sorted(l)
        self.assertEqual(my_sort, golden_sort)


class MyTest_Merge_Sort(unittest.TestCase):
    def test_int_list(self):
        l = list(np.random.randint(1000, size=1000))
        my_sort = merge_sort(l)
        golden_sort = sorted(l)
        self.assertEqual(my_sort, golden_sort)

    def test_float_list(self):
        l = list(np.random.random(size=999))
        my_sort = merge_sort(l)
        golden_sort = sorted(l)
        self.assertEqual(my_sort, golden_sort)


class MyTest_Bubble_Sort(unittest.TestCase):
    def test_int_list(self):
        l = list(np.random.randint(1000, size=1000))
        my_sort = bubble_sort(l)
        golden_sort = sorted(l)
        self.assertEqual(my_sort, golden_sort)

    def test_float_list(self):
        l = list(np.random.random(size=999))
        my_sort = bubble_sort(l)
        golden_sort = sorted(l)
        self.assertEqual(my_sort, golden_sort)


if __name__ == '__main__':
    unittest.main()
