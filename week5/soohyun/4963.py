# 백준 4963 섬의 개수
import sys
sys.setrecursionlimit(10 ** 6)

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]
    answer = 0
    dx = [-1, 0, 1, 0, -1, 1, 1, -1]
    dy = [0, -1, 0, 1, -1, -1, 1, 1]
    
    def dfs(x, y):
        if x <= -1 or x >= h or y <= -1 or y >= w:
            return False

        if graph[x][y] == 1:
            graph[x][y] = 0
            for i in range(8):
                dfs(x + dx[i], y + dy[i])
            return True
        return False

    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                answer += 1

    print(answer)