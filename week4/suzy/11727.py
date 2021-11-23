n = int(input())

# dp
dp = [0 for _ in range(1001)]
dp[1] = 1
dp[2] = 3

for i in range(3, 1001):
    # 점화식 2*1 직사각형과 2*2 직사각형 방법 두가지
    dp[i] = dp[i-1] + dp[i-2] * 2

print(dp[n] % 10007)


