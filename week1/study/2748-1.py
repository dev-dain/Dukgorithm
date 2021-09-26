# https://www.acmicpc.net/problem/2748
def fib(n):
  if n < 3: return 1
  return fib(n-1) + fib(n-2)

n = int(input())
print(fib(n))