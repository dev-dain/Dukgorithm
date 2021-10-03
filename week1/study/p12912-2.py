# https://programmers.co.kr/learn/courses/30/lessons/12912
def solution(a, b):
  if a == b: return a
  return (max(a,b) - min(a,b) + 1) * (a + b) / 2

a, b = map(int, input().split())
print(solution(a, b))