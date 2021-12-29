# 백준 2178 미로 탐색
from collections import deque

n, m = map(int, input().split()) # 세로, 가로
graph = [list(map(int, input())) for _ in range(n)] # 미로
# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(i, j):
    queue = deque([[i, j]]) # 시작 노드를 큐에 삽입

    while queue:
        x, y = queue.popleft() # 큐에서 노드를 가져온다
        # 동서남북으로 미로 탐색
        for i in range(4):
            # 이동할 위치 계산
            xi = x + dx[i]
            yi = y + dy[i]
            if xi <= -1 or xi >= n or yi <= -1 or yi >= m: # 이동할 수 있는 범위를 벗어난 경우
                continue
            if graph[xi][yi] == 1: # 이동할 수 있는 경우
                queue.append([xi, yi]) # 노드를 큐에 삽입
                graph[xi][yi] = graph[x][j] + 1 # 이동할 최소 칸 수를 구하기 위한 미로값 수정

# 전체 미로 탐색
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1: # 이동할 수 있다면 BFS 수행
            bfs(i, j)

print(graph[n-1][m-1])