""" 选择排序 """

def selectionSort(s):
    for i in range(len(s)):
        min_index = i
        min_value = s[i]
        for j in range(i, len(s)):
            if s[j] < min_value:
                min_value = s[j]
                min_index = j
        s[i], s[min_index] = s[min_index], s[i]
    return s


c = int(input())
for _ in range(c):
    s = list(map(int,input().split()))
    print(selectionSort(s))
