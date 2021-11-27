from collections import deque

def bfs(v):
    q = deque([v])
    # 현재 위치한 층을 방문처리
    visited[v] = 1

    while q:
        v = q.popleft()
        # 현재 층과 스타트링크층이 같다면 버튼 누를필요 X
        if v == g:
            return count[g]
        for i in (v+u, v-d): # u만큼 위로 or d만큼 아래로
            if 0 < i <= f and not visited[i]:
                visited[i] = 1
                count[i] = count[v] + 1
                q.append(i)


    if count[g] == 0:
        return "use the stairs"

# 총 층수 f, 강호 위치 s, 스타링크 g, 위로 u, 아래로 d
f, s, g, u, d = map(int, input().split())
visited = [0 for _ in range(f+1)]
count = [0 for _ in range(f+1)] # 버튼 누른 횟수
print(bfs(s))