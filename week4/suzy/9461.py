# dp
dp = [0 for i in range(101)] # 0부터 100의 범위
dp[1] = 1
dp[2] = 1
dp[3] = 1

# 점화식 f(n) = F(n-2) + f(n-3) (n>=3)
# [1,1,1,2,2,3,4,5,7,9,12,16....] 하나씩 돌면서 리스트를 만들어놓음.
for i in range(0, 98):
    dp[i+3] = dp[i] + dp[i+1]

# 테스트 케이스 t
t = int(input())
for i in range(t):
    i = int(input())
    print(dp[i])