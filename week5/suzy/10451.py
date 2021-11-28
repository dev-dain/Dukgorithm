import sys
sys.setrecursionlimit(10**7)

t = int(input())

def dfs(v):
    visited[v] = 1  #방문한 곳 1로 표시
    next = arr[v]
    if visited[next] == 0: #아직 방문하지 않은 곳인 경우
        dfs(next)

for i in range(t):
    answer = 0
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)

    for i in range(1, n+1):
        if visited[i] == 0:
            dfs(i)
            answer += 1
    print(answer) #순열 사이클의 개수