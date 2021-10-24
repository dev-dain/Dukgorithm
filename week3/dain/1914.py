# 10-15
import sys
sys.setrecursionlimit(10 ** 6)

def hanoi(start, end, aux, n):
  if n == 1:
    print(start, end)
    return
  
  hanoi(start, aux, end, n-1)
  print(start, end)
  hanoi(aux, end, start, n-1)

n = int(input())
print(pow(2, n)-1)
if n <= 20:
  hanoi(1, 3, 2, n)