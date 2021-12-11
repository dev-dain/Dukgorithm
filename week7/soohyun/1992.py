# 백준 1992 쿼드트리
N = int(input())
video = [list(map(int, input())) for _ in range(N)]
result = ''

def comp(x, y, n):
    global result
    state = video[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if video[i][j] != state:
                result += '('
                comp(x, y, n//2)
                comp(x, y+n//2, n//2)
                comp(x+n//2, y, n//2)
                comp(x+n//2, y+n//2, n//2)
                result += ')'
                return

    result += str(state)

comp(0, 0, N)
print(result)