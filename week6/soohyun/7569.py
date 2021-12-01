# 백준 7569 토마토
from collections import deque

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
queue = deque()
answer = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append([i, j, k])

def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            zi = z + dz[i]
            xi = x + dx[i]
            yi = y + dy[i]
            if zi <= -1 or zi >= h or xi <= -1 or xi >= n or yi <= -1 or yi >= m:
                continue
            if graph[zi][xi][yi] == 0:
                queue.append([zi, xi, yi])
                graph[zi][xi][yi] = graph[z][x][y] + 1

bfs()
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(j))
print(answer - 1)