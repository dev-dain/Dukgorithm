# bfs, deque
from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().split()) # n, m 입력받기

graph = [] # 2차원 배열로 nxm 크기의 미로생성
for _ in range(n):
    graph.append(list(map(int, stdin.readline().strip())))

# 상하좌우
h = [-1, 1, 0, 0]
w = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for d in range(4): #상하좌우
            xh = x + h[d]
            yw = y + w[d]
            if 0 <= xh < n and 0 <= yw < m:
                if graph[xh][yw] == 1: # 이동할 수 있는 '1'칸을 만족한다면 +1을 해준다.
                    graph[xh][yw] = graph[x][y] + 1
                    queue.append((xh,yw))

    return graph[n-1][m-1] # 목적지n, m의 값 출력

print(bfs(0,0))