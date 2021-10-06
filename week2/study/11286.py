import heapq, sys
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
  x = int(input())
  if x == 0:
    print(heapq.heappop(heap)[1]) if heap else print(0)
    continue
  # 힙을 튜플로 구성하면 맨앞숫자(abs(x))만 갖고 정렬하므로
  # 절댓값을 정렬 대상값으로 두도록 함
  # 힙에 들어가는 원소는 (절댓값, 수) 튜플
  heapq.heappush(heap, (abs(x), x))

  # 절댓값이라 음수가 안 나오기 때문에, 원래 숫자가 0과 가까울수록 우선순위가 높아짐
  # 절댓값이 똑같은 경우에는 원래 수(x)로 우선순위 계산
  # 이 때도 역시 수가 작은 것이 우선순위가 높기 때문에, 음수가 먼저 힙에서 탈출함