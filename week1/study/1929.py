# https://www.acmicpc.net/problem/1929
import math
m, n = map(int, input().split())

for i in range(m, n+1):
  for j in range(2, int(math.sqrt(i))+1):
    if i % j == 0:
      break
  else:
    print(i)