# 10-10
import heapq

def solution(scoville, K):
  heapq.heapify(scoville)
  cnt = 0
  while len(scoville) > 1:
    if scoville[0] < K:
      f1 = heapq.heappop(scoville)
      f2 = heapq.heappop(scoville)
      heapq.heappush(scoville, f1 + f2 * 2)
      cnt += 1
    else: 
      return cnt
  # 마지막 남은 음식이 K보다 클 수 있으므로 무작정 -1 하면 16번 테케가 틀림
  return -1 if scoville[0] < K else cnt

print(solution([1, 2, 3], 11))