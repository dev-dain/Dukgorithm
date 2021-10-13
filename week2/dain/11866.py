from collections import deque

n, k = map(int, input().split())
qu = deque(range(1, n+1))
lst = []
while qu:
  qu.rotate(-k) # 3씩 왼쪽으로 옮김
  lst.append(str(qu.pop())) # 맨 뒤에 있는 것이 뽑을 숫자임. 리스트에 넣어주기
print(f'<{", ".join(lst)}>')