""" 查找第一个大于等于给定值的元素 """


def bSearchV3(s, k):
    low = 0
    high = len(s) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if s[mid] < k:
            low = mid + 1
        else:
            if mid == 0 or s[mid - 1] < k:
                return mid
            else:
                high = mid - 1
    return -1


for _ in range(int(input())):
    s = list(map(int, input().split()))
    k = int(input())
    print(bSearchV3(s, k))
