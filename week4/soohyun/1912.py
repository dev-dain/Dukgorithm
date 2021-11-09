# 백준 1912 연속합
n = int(input())
nums = list(map(int, input().split()))
dp = [n for n in nums]

for i in range(1, n):
	dp[i] = max(dp[i], dp[i-1] + nums[i])
print(max(dp))