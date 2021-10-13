# 프로그래머스 42626 더 맵게
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K: # 모든 스코빌 지수가 K 이상이 될 때까지 반복
        if len(scoville) == 1: # 모든 음식의 스코빌 지수를 K이상으로 만들 수 없는 경우
            return -1
        
        mix = heapq.heappop(scoville) + 2 * heapq.heappop(scoville) # 스코빌 지수 계산
        heapq.heappush(scoville, mix)
        answer += 1
    
    return answer