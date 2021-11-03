# 백준 11726 2xn 타일링
n = int(input())
dp = [0] * (n+1)

if n <= 2:
	print(n)
else:
	dp[1], dp[2] = 1, 2
	for i in range(3, n+1):
		dp[i] = dp[i-1] + dp[i-2]
	print(dp[n] % 10007)