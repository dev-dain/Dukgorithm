# 삼각형의 크기
n = int(input())
# 정수 삼각형 리스트
li = []
for _ in range(n):
    li.append(list(map(int, input().split())))

# dp
dp = [0 for _ in range(501)]
# 맨위값
dp[0] = li[0][0]

for i in range(1, n):
    for j in range(len(li[i])):
        # 맨 왼쪽 더하기
        if j == 0:
            li[i][j] += li[i-1][j]
            continue
        # 맨 오른쪽 더하기
        if j == len(li[i])-1:
            li[i][j] += li[i-1][j-1]
            continue

        # 그 외 점화식
        li[i][j] += max(li[i-1][j-1], li[i-1][j])

print(max(li[n-1]))




