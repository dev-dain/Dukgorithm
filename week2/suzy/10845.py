# 입력 받기
import sys
n = int(sys.stdin.readline())

que = []
for _ in range(n):
    c = sys.stdin.readline().split()

    if c[0] == 'push':
        que.insert(0, c[1])
    elif c[0] == 'pop':
        if len(que) != 0:
            print(que.pop())
        else:
            print(-1)
    elif c[0] == 'size':
        print(len(que))
    elif c[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[len(que)-1])
    elif c[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])