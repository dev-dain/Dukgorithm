import sys
from collections import deque, defaultdict

# bfs
def bfs(start, g):
    # 큐 구현을 위해 deque 라이브러리 사용
    q = deque([start])
    visited= []

    # 큐가 빌때까지 반복
    while q:
        v = q.popleft()
        if v in visited:
            continue
        visited.append(v)

        # 아직 방문하지 않은 인접한 원소들 큐에 삽입
        for n in g[v]:
            if n not in visited:
                q.append(n)
    return visited

# 컴퓨터 수
n = int(sys.stdin.readline())
# 연결되어 있는 컴퓨터의 쌍
m = int(sys.stdin.readline())

g = defaultdict(list)

# 양방향 그래프 입력받기
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    g[a].append(b)
    g[b].append(a)

visited = bfs(1, g)

print(len(visited)-1)