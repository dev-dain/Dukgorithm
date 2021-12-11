# 백준 2512 예산
N = int(input())
money = list(map(int, input().split()))
M = int(input())
low, high = 1, max(money)

while low <= high:
    mid = (low + high) // 2
    s = sum([mid if mid < m else m for m in money])

    if s <= M:
        low = mid + 1
    else:
        high = mid - 1

print(high)