import math
n, S = map(int, input().split())
pos = list(map(int, input().split()))
dif = list(set(abs(p - S) for p in pos))

D = min(dif)

for d in dif:
	D = math.gcd(d, D)
print(D)