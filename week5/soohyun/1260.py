# 백준 1260 DFS와 BFS
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()

def dfs(start):
    visited[start] = 1
    print(start, end=' ')

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    queue = [start]
    visited[start] = 1

    while queue:
        node = queue.pop(0)
        print(node, end=' ')
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1

dfs(v)
print()
visited = [0] * (n+1)
bfs(v)