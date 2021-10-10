# 프로그래머스 42587 프린터
def solution(priorities, location):
    pr = [(p, i) for i, p in enumerate(priorities)] # (우선순위, 인덱스)의 대기목록
    queue = [] # 프린트 될 순서 리스트
    
    while pr:
        p = [p for p, i in pr]
        now = pr.pop(0) # 현재 문서
        
        if now[0] >= max(p): # 대기목록의 최대 우선순위보다 높다면 인덱스를 큐에 삽입
            queue.append(now[1])
        else: # 그렇지 않다면 대기목록에 삽입
            pr.append(now)
            
    return queue.index(location) + 1