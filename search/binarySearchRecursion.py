
def binarySearch(s, k):
    return binarySearch_c(s, 0, len(s) - 1, k)


def binarySearch_c(s, low, high, k):
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if s[mid] == k:
        return mid
    elif s[mid] > k:
        return binarySearch_c(s, low, mid - 1, k)
    else:
        return binarySearch_c(s, mid + 1, high, k)


for _ in range(int(input())):
    s = list(map(int, input().split()))
    k = int(input())
    print(binarySearch(s, k))
