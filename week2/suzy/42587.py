from collections import deque

def solution(priorities, location):
    answer = 0
    # 우선순위와 인덱스
    d = deque([(v, i) for i, v in enumerate(priorities)])

    while len(d):
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer
