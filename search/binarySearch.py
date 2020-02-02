
def binarySearch(s, k):
    low = 0
    high = len(s) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if s[mid] == k:
            return mid
        elif s[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return -1


for _ in range(int(input())):
    s = list(map(int, input().split()))
    k = int(input())
    print(binarySearch(s, k))
