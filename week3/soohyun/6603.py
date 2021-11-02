# 백준 6603 로또
from itertools import combinations

while True:
	nums = list(map(int, input().split()))

	if nums[0] == 0: break
		
	S = list(combinations(nums[1::], 6))
	for s in S:
		print(*s)
	print()