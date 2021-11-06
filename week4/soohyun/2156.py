# 백준 2156 포도주 시식
n = int(input())
wine = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)

if n == 1:
	print(wine[1])
else:
	dp[1] = wine[1]
	dp[2] = wine[1] + wine[2]
	# 최대로 마실 수 있는 포도주의 양 구하기
	for i in range(3, n+1):
		dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])
	print(max(dp))