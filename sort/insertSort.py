
def insertSort(s):
    for i in range(1, len(s)):
        value = s[i]
        j = i - 1
        while j >= 0 and s[j] > value:
            s[j + 1] = s[j]
            j -= 1
        s[j+1] = value
    return s


c = int(input())
for _ in range(c):
    s = list(map(int,input().split()))
    insertSort(s)
    print(s)
