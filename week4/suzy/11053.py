import sys
from collections import defaultdict

n = int(sys.stdin.readline())
# n만큼 수열
nlist = list(map(int, sys.stdin.readline().split()))

# dp 초기화
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        # 현재 > 이전 이라면 (크거나 같으면 가장 긴 증가하는 부분수열x)
        if nlist[i] > nlist[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))