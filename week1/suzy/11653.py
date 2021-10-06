n = int(input())
# 가장 작은 소수 2부터 시작
d = 2

while d <= n:
    if n % d == 0:
        print(d)
        # 다음 몫
        n /= d
    else:
        # 2로 나누어지지 못할 경우
        d = d + 1
