# 백준 2193 이친수
n = int(input())
dp = [0] * (n+1)

if n <= 2:
	print(1)
else:
	dp[1], dp[2] = 1, 1
	for i in range(3, n+1):
		dp[i] = dp[i-1] + dp[i-2]
	print(dp[n])