# 이거 18258이랑 똑같은데 시간제한이 더 빡셈
# 일단 입력 가속을 해야함
import sys
input = sys.stdin.readline
from collections import deque

queue = deque()
n = int(input())
# 리스트 컴프리헨션으로 하면 시간초과
# 매 루프마다 명령을 처리해야 시간초과 안뜸
for _ in range(n):
  order = input().split()

  # 만약 order가 2개로 쪼개진다면 append하는 것임
  if len(order) != 1:
    queue.append(int(order[1]))
  elif order[0] == 'pop':
    print(queue.popleft()) if len(queue) else print(-1)
  elif order[0] == 'size':
    print(len(queue))
  elif order[0] == 'empty':
    print(0) if len(queue) else print(1)
  elif order[0] == 'front':
    print(queue[0]) if len(queue) else print(-1)
  elif order[0] == 'back':
    print(queue[-1]) if len(queue) else print(-1)