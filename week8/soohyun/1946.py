# 백준 1946 신입사원
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    rank = [list(map(int, input().split())) for _ in range(N)]
    rank.sort()
    count = 1

    max = rank[0][1]
    for i in range(1, N):
        if rank[i][1] < max:
            count += 1
            max = rank[i][1]

    print(count)