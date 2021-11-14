# 백준 11727 2xn 타일링 2
n = int(input())
dp = [1] * (n+1)

if n <= 1:
	print(1)
else:
	dp[1] = 1
	for i in range(2, n+1):
		dp[i] = dp[i-1] + dp[i-2] * 2
	print(dp[n] % 10007)