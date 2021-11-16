import sys
from collections import defaultdict, deque

def bfs(start):
    cnt = 0
    # 각 노드가 방문된 정보를 표현
    visited = [0 for _ in range(n+1)]
    # 현재 노드를 방문 처리
    visited[start] = 1
    queue = deque([[start, 0]])
    # 큐가 빌때까지 반복
    while queue:
        # 친구와 거리
        u, dist = queue.popleft()

        if dist <= 2: # 친구의 친구(dist==2)까지 초대할 수 있다
            cnt += 1
        for v in g[u]:
            if not visited[v]:
                visited[v] = 1
                queue.append([v, dist+1])
    return cnt-1 # cnt 자기자신 -1

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
g = defaultdict(list)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    g[a].append(b)
    g[b].append(a)

print(bfs(1))
