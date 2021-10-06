from collections import deque

n = int(input())
qu = deque(range(1,n+1))  # 1부터 n까지 숫자 카드 리스트를 만듦

# 카드 묶음에 카드가 2개 이상인 동안
while len(qu) > 1:
  qu.popleft()  # 카드 한 장 제거
  qu.rotate(-1) # 맨 위의 카드를 맨 뒤로 뺌
print(qu[0])  # 마지막 남은 카드 1장 출력