# 덱 내장 모듈
from collections import deque

n = int(input())
d = deque()
for i in range(1,n+1):
    d.append(i)
print(list(d))
