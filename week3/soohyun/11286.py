# 백준 11286 절대값 힙
import heapq, sys

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
	x = int(sys.stdin.readline())

	if x == 0: # 절대값이 가장 작은 값 출력
		if len(heap) == 0:
			print(0)
		else:
			print(heapq.heappop(heap)[1])
	else: # 힙에 값 추가
		heapq.heappush(heap, (abs(x), x))