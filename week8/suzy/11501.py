t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    max_value = s[-1]
    add = 0

    for i in range(len(s)-2, -1, -1):
        if s[i] > max_value:
            max_value = s[i]
        # 이득일 경우에는 파는 것을 더해줌
        else:
            add += max_value-s[i]

    print(add)
