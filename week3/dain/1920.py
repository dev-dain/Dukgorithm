# 09-06
import sys
input = sys.stdin.readline

n = int(input())
a = sorted(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

for num in b:
  low = 0
  high = len(a) - 1
  flag = 0
  while low <= high:
    mid = (low + high) // 2
    if a[mid] == num:
      flag = 1
      break
    elif a[mid] > num:
      high = mid - 1      
    else:
      low = mid + 1
  print(flag)