import sys
sys.setrecursionlimit(10**6)

def star(l):
  if l == 1: return ['*']

  stars = star(l // 3)
  result = []

  for s in stars:
    result.append(s*3)
  for s in stars:
    result.append(s + ' ' * (l//3) + s)
  for s in stars:
    result.append(s*3)
  return result

n = int(input())
print('\n'.join(star(n)))