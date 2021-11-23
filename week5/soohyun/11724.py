# 백준 11724 연결 요소의 개수
n , m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
answer = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    global answer
    queue = [start]
    visited[start] = 1

    while queue:
        v = queue.pop(0)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
    return True

for i in range(1, n+1):
    if visited[i] == 0 and bfs(i) == True:
        answer += 1

print(answer)