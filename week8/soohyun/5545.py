# 백준 5545 최고의 피자
N = int(input())
A, B = map(int, input().split())
C = int(input())
D = [int(input()) for _ in range(N)]
D.sort(reverse=True)

cal = C
price = A
for d in D:
    if (cal+d) / (price + B) > cal / price:
        cal += d
        price += B

print(cal // price)