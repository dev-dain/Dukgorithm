# 백준 4485 녹색 옷 입은 애가 젤다지?
import sys, heapq

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
count = 1

def dijkstra():
    queue = []
    heapq.heappush(queue, (graph[0][0], 0, 0))
    dist[0][0] = graph[0][0]

    while queue:
        cur_dist, x, y = heapq.heappop(queue)
        if cur_dist > dist[x][y]:
            continue
        for i in range(4):
            xi = x + dx[i]
            yi = y + dy[i]
            if 0 <= xi < n and 0 <= yi < n:
                cost = cur_dist + graph[xi][yi]
                if cost < dist[xi][yi]:
                    heapq.heappush(queue, (cost, xi, yi))
                    dist[xi][yi] = cost

while True:
    n = int(input())
    if n == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(n)]
    dist = [[sys.maxsize] * n for _ in range(n)]

    dijkstra()
    print(f'Problem {count}: {dist[n-1][n-1]}')
    count += 1