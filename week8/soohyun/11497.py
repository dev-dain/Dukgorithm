# 백준 11497 통나무 건너뛰기
T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    answer = 0

	# 최소 난이도 구하기
    for i in range(2, N):
        answer = max(answer, nums[i] - nums[i-2])
    print(answer)