# 백준 11501 주식
T = int(input())

for _ in range(T):
    N = int(input())
    days = list(map(int, input().split()))
    money = 0
    max = 0

    for i in range(N-1, -1, -1):
        if days[i] > max:
            max = days[i]
        else:
            money += max - days[i]

    print(money)