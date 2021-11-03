# dp
dp = [0 for i in range(12)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

# 점화식 f(n) = F(n-1) + f(n-2) + f(n-3)
for i in range(4, 12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

# 테스트 케이스 t
t = int(input())
for i in range(t):
    n = int(input())
    print(dp[n])