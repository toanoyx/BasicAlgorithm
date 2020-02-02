""" 计数排序 """


def countingSort(s):
    c = [0] * (max(s) + 1)  # 计数数组
    r = [0] * len(s)    # 临时数组，存放排序之后的结果
    for num in s:
        c[num] += 1
    for i in range(1, len(c)):
        c[i] = c[i] + c[i - 1]
    for num in reversed(s):
        r[c[num] - 1] = num
        c[num] -= 1
    s[:] = r
    return s


for _ in range(int(input())):
    s = list(map(int, input().split()))
    countingSort(s)
    print(s)
