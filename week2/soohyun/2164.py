# 백준 2164 카드 2
from collections import deque

n = int(input())
nums = deque([i for i in range(1, n+1)])

while True:
	if len(nums) == 1: # 값이 1개 남으면 break
		break
		
	nums.popleft() # 제일 위에 있는 카드 버리기
	# 그 다음 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮기기
	top = nums.popleft()
	nums.append(top)

print(*list(nums))