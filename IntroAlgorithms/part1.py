import numpy as np
from my_exception import *


def instersion_sort(a_list):
    for j in range(1, len(a_list)):
        key = a_list[j]
        i = j-1
        while i >= 0 and a_list[i] > key:
            a_list[i+1] = a_list[i]
            i = i-1
        a_list[i+1] = key
    return a_list


def selection_sort(a_list):
    for j in range(0, len(a_list)-1):
        smallest = j
        for i in range(j+1, len(a_list)):
            if a_list[i] < a_list[smallest]:
                smallest = i
        tmp = a_list[j]
        a_list[j] = a_list[smallest]
        a_list[smallest] = tmp
    return a_list


def merge(left_list, right_list):
    merge_list = []
    i = j = 0
    for k in range(len(left_list)+len(right_list)+1):
        if left_list[i] <= right_list[j]:
            merge_list.append(left_list[i])
            i += 1
            if i >= len(left_list):
                merge_list += right_list[j:]
                break
        else:
            merge_list.append(right_list[j])
            j += 1
            if j >= len(right_list):
                merge_list += left_list[i:]
                break
    return merge_list


def merge_sort(a_list):
    if len(a_list) <= 1:
        return a_list
    half_index = int(len(a_list)/2)
    left = a_list[:half_index]
    right = a_list[half_index:]
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    return merge(left_sorted, right_sorted)


def bubble_sort(a_list):
    for i in range(0, len(a_list)-1):
        for j in range(len(a_list)-1, i, -1):
            if a_list[j] < a_list[j-1]:
                tmp = a_list[j]
                a_list[j] = a_list[j-1]
                a_list[j-1] = tmp
    return a_list


def find_max_crossing_subarray(a_list, low, mid, high):
    left_sum = sum = a_list[mid]
    max_left = mid
    for i in range(mid-1, low-1, -1):
        sum = sum+a_list[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = sum = a_list[mid+1]
    max_right = mid+1
    for i in range(mid+2, high+1, 1):
        sum = sum+a_list[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i
    return (max_left, max_right, left_sum+right_sum)


def find_max_subarray(a_list, low, high):
    if(high == low):
        return (low, high, a_list[low])
    else:
        mid = int((low+high)/2)
        (left_low, left_high, left_sum) = find_max_subarray(a_list, low, mid)
        (right_low, right_high, right_sum) = find_max_subarray(a_list, mid+1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(
            a_list, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        if right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)


def square_matrix_multiply(a, b):
    if a.shape != b.shape:
        raise NotSameSizeError('two matrix are not same size')
    n = a.shape[0]
    m = a.shape[1]
    if not n == m:
        raise NotSquareError('matrix is not square')
    c = np.zeros(a.shape)
    for i in range(n):
        for j in range(n):
            c[i][j] = 0
            for k in range(n):
                c[i][j] += a[i][k]*b[k][j]
    return c


def square_matrix_multiply_recursive(a, b):
    if a.shape != b.shape:
        raise NotSameSizeError('two matrix are not same size')
    n = a.shape[0]
    m = a.shape[1]
    if not n == m:
        raise NotSquareError('matrix is not square')
    if n & (n-1) != 0:
        raise NotPowOfTwoError('matrix row/cloumn is not power of 2')

    c = np.zeros(a.shape)
    if n == 1:
        c = a*b
        return c
    else:
        h = int(n/2)
        a11 = a[:h, :h]
        a12 = a[:h, h:]
        a21 = a[h:, :h]
        a22 = a[h:, h:]
        b11 = b[:h, :h]
        b12 = b[:h, h:]
        b21 = b[h:, :h]
        b22 = b[h:, h:]

        c[:h, :h] = \
            square_matrix_multiply_recursive(a11, b11) + \
            square_matrix_multiply_recursive(a12, b21)
        c[:h, h:] = \
            square_matrix_multiply_recursive(a11, b12) + \
            square_matrix_multiply_recursive(a12, b22)
        c[h:, :h] = \
            square_matrix_multiply_recursive(a21, b11) + \
            square_matrix_multiply_recursive(a22, b21)
        c[h:, h:] = \
            square_matrix_multiply_recursive(a21, b12) + \
            square_matrix_multiply_recursive(a22, b22)
        return c


def square_matrix_multiply_strassen(a, b):
    if a.shape != b.shape:
        raise NotSameSizeError('two matrix are not same size')
    n = a.shape[0]
    m = a.shape[1]
    if not n == m:
        raise NotSquareError('matrix is not square')
    if n & (n-1) != 0:
        raise NotPowOfTwoError('matrix row/cloumn is not power of 2')

    c = np.zeros(a.shape)
    if n == 1:
        c = a*b
        return c
    else:
        h = int(n/2)
        a11 = a[:h, :h]
        a12 = a[:h, h:]
        a21 = a[h:, :h]
        a22 = a[h:, h:]
        b11 = b[:h, :h]
        b12 = b[:h, h:]
        b21 = b[h:, :h]
        b22 = b[h:, h:]

        p1 = square_matrix_multiply_strassen(a11, b12) - \
            square_matrix_multiply_strassen(a11, b22)

        p2 = square_matrix_multiply_strassen(a11, b22) + \
            square_matrix_multiply_strassen(a12, b22)

        p3 = square_matrix_multiply_strassen(a21, b11) + \
            square_matrix_multiply_strassen(a22, b11)

        p4 = square_matrix_multiply_strassen(a22, b21) - \
            square_matrix_multiply_strassen(a22, b11)

        p5 = square_matrix_multiply_strassen(a11, b11) + \
            square_matrix_multiply_strassen(a11, b22) + \
            square_matrix_multiply_strassen(a22, b11) + \
            square_matrix_multiply_strassen(a22, b22)

        p6 = square_matrix_multiply_strassen(a12, b21) + \
            square_matrix_multiply_strassen(a12, b22) - \
            square_matrix_multiply_strassen(a22, b21) - \
            square_matrix_multiply_strassen(a22, b22)

        p7 = square_matrix_multiply_strassen(a11, b11) + \
            square_matrix_multiply_strassen(a11, b12) - \
            square_matrix_multiply_strassen(a21, b11) - \
            square_matrix_multiply_strassen(a21, b12)

        c[:h, :h] = p5+p4-p2+p6
        c[:h, h:] = p1+p2
        c[h:, :h] = p3+p4
        c[h:, h:] = p5+p1-p3-p7
        return c


def main():
    m_size = (4, 4)
    a = np.random.randint(-100, 100, size=m_size)
    b = np.random.randint(-100, 100, size=m_size)
    c1 = square_matrix_multiply_strassen(a, b)
    c2 = square_matrix_multiply(a, b)
    print(a)
    print(b)
    print(c1)
    print(c2)

    # h = int(a.shape[0]/2)
    # print(a)
    # # print(b)
    # print('h=%d' % h)
    # a11 = a[:h, :h]
    # a12 = a[:h, h:]
    # a21 = a[h:, :h]
    # a22 = a[h:, h:]
    # print(a11)
    # print(a12)
    # print(a21)
    # print(a22)


if __name__ == '__main__':
    main()
