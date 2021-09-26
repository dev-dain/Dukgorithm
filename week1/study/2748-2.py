# https://www.acmicpc.net/problem/2748
n = int(input())
a = b = result = 1
for i in range(3, n+1):
  result = a + b
  a = b
  b = result
print(result)