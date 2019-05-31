import numpy as np


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
    n = a.shape[0]
    c = np.zeros(a.shape)
    for i in range(n):
        for j in range(n):
            c[i][j] = 0
            for k in range(n):
                c[i][j] += a[i][k]*b[k][j]
    return c


def main():
    a = np.random.randint(-100, 100, size=(3, 3))
    b = np.random.randint(-100, 100, size=(3, 3))
    c = square_matrix_multiply(a, b)
    d = np.matmul(a, b)
    print(c)
    print(d)

    print((c == d).all())


if __name__ == '__main__':
    main()
