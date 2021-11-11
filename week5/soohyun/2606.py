# 백준 2606 바이러스
from collections import defaultdict, deque

n  = int(input())
e = int(input())
graph = defaultdict(list)

for _ in range(e):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

def bfs(graph, start):
	visited = []
	q = deque([start])

	while q:
		node = q.popleft()
		if node not in visited:
			visited.append(node)
			q += graph[node]

	return len(visited) - 1

result = bfs(graph, 1)
print(result)