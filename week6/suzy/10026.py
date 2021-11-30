# bfs, deque
from collections import deque

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q.append([x, y])
    visited[x][y] = cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == graph[x][y] and visited[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = 1

n = int(input())
graph = [list(map(str, input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
q = deque()

cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt, end=' ')

# R > G 적록색약
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'
visited = [[0]*n for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt)