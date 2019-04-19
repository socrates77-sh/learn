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


def main():
    l = list(np.random.randint(1000, size=7))
    r = instersion_sort(list(np.random.randint(1000, size=10)))
    # print(l, r)
    # m = merge(l, r)
    # print(m)
    # print(len(m))
    print(l)
    print(bubble_sort(l))


if __name__ == '__main__':
    main()
