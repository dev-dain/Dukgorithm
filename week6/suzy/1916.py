import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드 개수 n 간선 개수 m
n = int(input())
m = int(input())

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # a -> b 비용 c
    graph[a].append((b, c))
# 출발지와 도착지
start, end = map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 시작지점 힙에 추가

    while q:
        # 거리, 현재 노드
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

print(distance[end])