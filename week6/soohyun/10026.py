# 백준 10026 적록색약
from collections import deque

n = int(input())
no_rg = [list(input()) for _ in range(n)]
yes_rg = [[''] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if no_rg[i][j] == 'R' or no_rg[i][j] == 'G':
            yes_rg[i][j] = 'R'
        else:
            yes_rg[i][j] = 'B'

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = [0] * 2

def bfs(graph, i, j, c):
    queue = deque([[i, j]])
    graph[i][j] = 'F'

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            xi = x + dx[i]
            yi = y + dy[i]
            if xi <= -1 or xi >= n or yi <= -1 or yi >= n:
                continue
            if graph[xi][yi] == c:
                queue.append([xi, yi])
                graph[xi][yi] = 'F'

for i in range(n):
    for j in range(n):
        if no_rg[i][j] != 'F':
            bfs(no_rg, i, j, no_rg[i][j])
            answer[0] += 1
        if yes_rg[i][j] != 'F':
            bfs(yes_rg, i, j, yes_rg[i][j])
            answer[1] += 1

print(*answer)