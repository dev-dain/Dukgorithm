# 조합 이용
from itertools import combinations as cb

n, s = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0

for i in range(1, n+1):
    # cb(list,i) // list 에서 i만큼 추출
    for combination in cb(nums, i):
        if sum(combination) == s:
            # print(combination) 조건에 만족하는 경우의 수 확인
            cnt += 1
print(cnt)