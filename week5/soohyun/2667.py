# 백준 2667 단지번호 붙이기
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
answer = [] # 단지 내 집의 수 리스트
count = result = 0 # 각 단지내 집의 수, 총 단지 수
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n: # 이동할 범위를 벗어난 경우
        return False

    if graph[x][y] == 1: # 집이 있다면
        global count
        count += 1
        graph[x][y] = 0 # 방문 처리를 해준다
        for i in range(4): # 좌, 우, 아래, 위 집을 방문한다
            dfs(x + dx[i], y + dy[i])
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            answer.append(count)
            result += 1
            count = 0

answer.sort()
print(result)
print(*answer)     