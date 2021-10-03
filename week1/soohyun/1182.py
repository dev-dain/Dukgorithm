# 백준 1182 부분수열의 합
from itertools import combinations

n, S = map(int, input().split())
nums = list(map(int, input().split()))
count = 0 # 합이 S인 부분 수열의 개수

for i in range(1, n+1): # i는 조합할 개수
	for cb in list(combinations(nums, i)): # cb는 조합한 수들
		if sum(cb) == S: # 조합한 수들의 합이 S와 같다면
			count += 1
print(count)