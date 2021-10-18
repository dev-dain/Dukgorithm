# 10-09
import sys
input = sys.stdin.readline

n = int(input())
serial = [input().strip() for _ in range(n)]
serial.sort(key=lambda x: (len(x), sum([int(c) for c in x if c.isdigit()]), x))
for s in serial:
  print(s)