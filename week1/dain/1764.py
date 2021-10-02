# 10-02
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
h = set(input().strip() for _ in range(n))
s = set(input().strip() for _ in range(m))
hs = sorted(list(h & s))
print(len(hs))
for p in hs:
  print(p)