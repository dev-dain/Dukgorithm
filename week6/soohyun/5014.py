# 백준 5014 스타트링크
from collections import deque

F, S, G, U, D = map(int, input().split())
dist = [0] * (F+1)

def bfs(start):
    queue = deque([[start, 0]])
    dist[start] = 1

    while queue:
        x, count = queue.popleft()
        if x == G:
            return count

        if x + U <= F and not dist[x + U]:
            queue.append([x + U, count + 1])
            dist[x + U] = 1
        if  x - D >= 1 and not dist[x - D]:
            queue.append([x - D, count + 1])
            dist[x - D] = 1

    return 'use the stairs'

answer = bfs(S)
print(answer)