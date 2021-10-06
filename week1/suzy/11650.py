# 시간 초과
n = int(input())
# x 좌표와 y좌표 담을 2차원 배열
nums = []

for i in range(n):
    [x, y] = map(int, input().split())
    nums.append([x, y])

    nums = sorted(nums)

for i in range(n):
    print(nums[i][0], nums[i][1])