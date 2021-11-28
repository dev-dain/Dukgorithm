import sys
# 런타임에러
sys.setrecursionlimit(10000)
def dfs(i, j, h, w):
    # 방향 벡터
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    m[i][j] = 0

    for n in range(8):
        ni = dx[n] + i
        nj = dy[n] + j
        # 지도를 벗어나는 경우
        if  0 <= ni < h and 0 <= nj < w and m[ni][nj] == 1:
            dfs(ni, nj, h, w)

# 지도넓이 w, 높이 h
while True:
    w, h = map(int, sys.stdin.readline().split())
    if h == 0 and w == 0:
        break

    m = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]

    cnt = 0

    for i in range(h):
        for j in range(w):
            if m[i][j] == 1:
                dfs(i, j, h, w)
                cnt += 1
    print(cnt)
