#백준 17087
#숨바꼭질 6

from math import gcd

N, S = map(int, input().split())
bro = list(map(int, input().split()))

ans = abs(S - bro[0])
for i in range(1, len(bro)):
    ans = gcd(ans, abs(S-bro[i]))

print(ans)