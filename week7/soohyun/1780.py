# 백준 1780 종이의 개수
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
minus, zero, one = 0, 0, 0

def divide(x, y, n):
    global minus, zero, one
    state = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != state:
                divide(x, y, n//3)
                divide(x, y+n//3, n//3)
                divide(x, y+n//3*2, n//3)
                divide(x+n//3, y, n//3)
                divide(x+n//3, y+n//3, n//3)
                divide(x+n//3, y+n//3*2, n//3)
                divide(x+n//3*2, y, n//3)
                divide(x+n//3*2, y+n//3, n//3)
                divide(x+n//3*2, y+n//3*2, n//3)
                return

    if state == -1:
        minus += 1
    elif state == 0:
        zero += 1
    else:
        one += 1

divide(0, 0, N)
print(minus)
print(zero)
print(one)