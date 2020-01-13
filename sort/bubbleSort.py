
def bubbleSort(s):
    for i in range(len(s)):
        for j in range(len(s) - i - 1):
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]
    return s


c = int(input())
for _ in range(c):
    s = list(map(int,input().split()))
    bubbleSort(s)
    print(s)
