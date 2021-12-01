# 백준 7576 토마토
from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
queue = deque()
answer = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            xi = x + dx[i]
            yi = y + dy[i]
            if xi <= -1 or xi >= n or yi <= -1 or yi >= m:
                continue
            if graph[xi][yi] == 0:
                queue.append([xi, yi])
                graph[xi][yi] = graph[x][y] + 1

bfs()
for g in graph:
    for v in g:
        if v == 0:
            print(-1)
            exit(0)
    answer = max(answer, max(g))
print(answer - 1)