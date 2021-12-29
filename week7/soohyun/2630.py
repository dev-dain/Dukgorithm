# 백준 2630 색종이 만들기
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white, blue = 0, 0

def divide(x, y, n):
    global white, blue
    color = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != color:
                divide(x, y, n//2)
                divide(x, y+n//2, n//2)
                divide(x+n//2, y, n//2)
                divide(x+n//2, y+n//2, n//2)
                return

    if color == 0:
        white += 1
    else:
        blue += 1

divide(0, 0, N)
print(white)
print(blue)