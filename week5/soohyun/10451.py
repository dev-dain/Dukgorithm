# 백준 10451 순열 사이클
t = int(input())

def bfs(start):
	queue = [start]
	visited[start] = 1

	while queue:
		v = queue.pop(0)
		next = graph[v]

		if not visited[next]:
			queue.append(next)
			visited[next] = 1

	return 1

for _ in range(t):
	n = int(input())
	graph = [0] + list(map(int, input().split()))
	visited = [0] * (n+1)
	answer = 0

	for i in range(1, n+1):
		if not visited[i]:
			answer += bfs(i)

	print(answer)