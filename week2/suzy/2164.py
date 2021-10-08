# 덱 내장 모듈
from collections import deque

n = int(input())
d = deque()
# 1부터 n까지 덱
for i in range(n):
    d.append(i+1)

while len(d)>1:
    # 맨 위 카드를 꺼내고 아래로 옮기기
    d.popleft()
    d.rotate(-1)
print(d.pop())

