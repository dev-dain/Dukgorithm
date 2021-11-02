import sys
import heapq
# 연산의 개수 N
N = int(sys.stdin.readline())
heap = []
# heap 리스트를 힙으로
heapq.heapify(heap)

for i in range(N):
    n = int(sys.stdin.readline())
    if n:
        # 절댓값이므로 우선순위는 abs(n)
        # 힙큐에 값은 ( 절대값, 원래값 )
        heapq.heappush(heap, (abs(n), n))
    else:
        if heap:
            # 절댓값이 가장 작은 값
            print(heapq.heappop(heap)[1])
        else:
            # 배열이 비어있는 경우 0
            print(0)

