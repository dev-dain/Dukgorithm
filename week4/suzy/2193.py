import sys
n = int(sys.stdin.readline())

# dp
dp = [1 for i in range(91)] # 0부터 90의 범위
dp[1] = 1 # 1
dp[2] = 1 # 10
# dp[3] = 2 # 100 101
# dp[4] = 3 # 1000 1001 1010
# dp[5] = 5 # 10000 10001 10010 10100 10101

for i in range(1, n+1):
    if i == 1 or i == 2:
        dp[i] = 1
    else:
        dp[i] = dp[i-1] + dp[i-2]

print(dp[i])
