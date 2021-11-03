# 백준 9095 1,2,3 더하기
t = int(input())

for _ in range(t):
	n = int(input())
	dp = [1] * (n+1)

	if n <= 2:
		print(n)
	else:
		dp[1], dp[2] = 1, 2
		for i in range(3, n+1):
			dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
		print(dp[i])