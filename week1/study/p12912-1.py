# https://programmers.co.kr/learn/courses/30/lessons/12912
def solution(a, b):
  if a == b: return a
  return sum(range(min(a, b), (max(a, b)+1)))

a, b = map(int, input().split())
print(solution(a, b))