import sys

n = int(sys.stdin.readline())
arr = list(map(int, input().split()))
arr2 = list(sorted(set(arr)))

dic = {arr2[i]: i for i in range(len(arr2))}

for i in arr:
    print(dic[i], end=" ")