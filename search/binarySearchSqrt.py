
def binarySearchSqrt(n):
    low = 1
    high = 100
    while low <= high:
        mid = low + (high - low) // 2
        if mid ** 2 == n:
            return mid
        elif mid ** 2 < n:
            low = mid + 1
        else:
            high = mid -1
    return -1


for _ in range(int(input())):
    print("please input one number between 1 - 10000")
    n = int(input())
    print(binarySearchSqrt(n))
