# 09-25
import heapq, sys
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
  x = int(input())
  if x == 0:
    # 그러면 두 번째가 원래 값이 됨
    print(heapq.heappop(heap)[1]) if heap else print(0)
    continue
  # 힙을 튜플로 구성하면 맨앞숫자만 갖고 정렬하므로
  # 절댓값을 정렬 대상값으로 두도록 함
  heapq.heappush(heap, (abs(x), x))