""" 归并排序 """


def mergeSort(s):
    mergeSort_c(s, 0, len(s) - 1)


def mergeSort_c(s, low, high):
    if low < high:
        mid = low + (high - low) // 2
        mergeSort_c(s, low, mid)
        mergeSort_c(s, mid + 1, high)
        merge(s, low, mid, high)


def merge(s, low, mid, high):
    i, j = low, mid+1
    tmp = []
    while i <= mid and j <= high:
        if s[i] <= s[j]:
            tmp.append(s[i])
            i += 1
        else:
            tmp.append(s[j])
            j += 1
    if i <= mid:
        tmp.extend(s[i:mid + 1])
    else:
        tmp.extend(s[j:high + 1])
    s[low:high + 1] = tmp


c = int(input())
for _ in range(c):
    s = list(map(int, input().split()))
    mergeSort(s)
    print(s)
