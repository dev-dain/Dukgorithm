from collections import deque

# 가로 m 세로 n
m, n = map(int, input().split())
graph = []
q = deque([])
for i in range(n):
  graph.append(list(map(int, input().split())))

# 익은 토마토를 큐에 저장
  for j in range(m):
    if graph[i][j] == 1:
      q.append([i, j])

# 방향 벡터
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs():
  while q:
    x, y = q.popleft()
    for i in range(4):
      a = x + dx[i]
      b = y + dy[i]
      if 0 <=a<n and 0<=b<m and graph[a][b] == 0:
        q.append([a,b])
        graph[a][b] = graph[x][y]+1

bfs()
ans = 0
for i in graph:
  for j in i:
    if j == 0:
      print(-1)
      exit(0)
  ans = max(ans, max(i))

print(ans-1)