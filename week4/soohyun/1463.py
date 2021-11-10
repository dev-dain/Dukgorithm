# 백준 1463 1로 만들기
n = int(input())
dp = [0] * (n+1)

for i in range(2, n+1):
	dp[i] = dp[i-1] + 1 # 2와 3으로 나누어 떨어지지 않는 경우 무조건 1을 빼줘야 하므로 횟수를 추가한다

	if i % 2 == 0: # 2로 나누어 떨어지는 경우
		dp[i] = min(dp[i], dp[i//2] + 1)
	if i % 3 == 0: # 3으로 나누어 떨어지는 경우
		dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])