# 백준 2470 두 용액
n = int(input())
sol = list(map(int, input().split()))
sol.sort()

left, right = 0, n-1
result = sol[left] + sol[right]
al, ar = left, right

while left < right:
    s = sol[left] + sol[right]

    if abs(s) < abs(result):
        result = s
        al = left
        ar = right

    if s < 0:
        left += 1
    else:
        right -= 1

print(sol[al], sol[ar])