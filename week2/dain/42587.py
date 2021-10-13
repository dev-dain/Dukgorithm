from collections import deque

def solution(priorities, location):
  # 우선순위와 뽑혀나가는 순서 덱 2개 만듦
  priorities = deque(priorities)
  orders = deque(list(range(len(priorities))))
  # 아예 여기는 인덱스를 다르게 처리함. 
  # 왜냐면 똑같은 숫자가 여러 개 있을 수 있기 때문에
  orders[location] = 't' 
  order = 0

  # 큐에 뭔가 있는 동안..
  while priorities:
    # 큐의 맨앞에 있는 것이 최고 우선순위라면
    if priorities[0] == max(priorities):
      order += 1  # 순번이 밀림. 실제로 pop할 때만 order 순번이 추가됨
      if orders[0] == 't':  # 만약 우리가 찾던 그 문서라면
        return order  # 바로 순번 출력
      priorities.popleft()  # 아니라면 그냥 뽑음
      orders.popleft()
    else:
      priorities.rotate(-1)
      orders.rotate(-1)