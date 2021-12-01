# 백준 1916 최소비용 구하기
from collections import defaultdict
import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = defaultdict(list)
dist = [sys.maxsize for _ in range(n+1)]

for _ in range(m):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
S, E = map(int, input().split())


def dijkstra(start):
    queue = []
    dist[start] = 0
    heapq.heappush(queue, (0, start))

    while queue:
        cur_dist, node = heapq.heappop(queue)
        if cur_dist > dist[node]:
            continue
        for next_node, next_dist in graph[node]:
            cost = cur_dist + next_dist
            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(queue, (cost, next_node))

dijkstra(S)
print(dist[E])