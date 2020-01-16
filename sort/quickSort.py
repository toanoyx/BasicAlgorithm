""" 快速排序 """

import random


def quickSort(s):
    quickSort_c(s, 0, len(s)-1)


def quickSort_c(s, low, high):
    if low < high:
        k = random.randint(low, high)
        s[low], s[k] = s[k], s[low]
        m = partition(s, low, high)
        quickSort_c(s, low, m - 1)
        quickSort_c(s, m + 1, high)


def partition(s, low, high):
    pivot, j = s[low], low
    for i in range(low + 1, high + 1):
        if s[i] <= pivot:
            j += 1
            s[j], s[i] = s[i], s[j]
    s[low], s[j] = s[j], s[low]
    return j


c = int(input())
for _ in range(c):
    s = list(map(int, input().split()))
    quickSort(s)
    print(s)
