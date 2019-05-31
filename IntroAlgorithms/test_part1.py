import unittest

import numpy as np
from part1 import *


class Part1_Instersion_Sort(unittest.TestCase):
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


class Part1_Selection_Sort(unittest.TestCase):
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


class Part1_Merge_Sort(unittest.TestCase):
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


class Part1_Bubble_Sort(unittest.TestCase):
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


class Part1_Find_Max_Subarray(unittest.TestCase):
    def test_normal_list(self):
        a_list = [13, -3, -25, 20, -3, -16, -23,
                  18, 20, -7, 12, -5, -22, 15, -4, 7]
        result = find_max_subarray(a_list, 0, len(a_list)-1)
        golden = (7, 10, 43)
        self.assertEqual(result, golden)

    def test_one_element_list(self):
        a_list = [13]
        result = find_max_subarray(a_list, 0, len(a_list)-1)
        golden = (0, 0, 13)
        self.assertEqual(result, golden)


class Par1_Maxtrix_Multiply(unittest.TestCase):
    def test_square_matrix_multiply(self):
        m_size = (10, 10)
        a = np.random.randint(-100, 100, size=m_size)
        b = np.random.randint(-100, 100, size=m_size)
        result = square_matrix_multiply(a, b)
        golden = np.matmul(a, b)
        self.assertTrue((result == golden).all())
