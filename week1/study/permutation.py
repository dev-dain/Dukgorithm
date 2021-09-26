from itertools import permutations, combinations
n = int(input())
for combi in combinations(range(1, n+1), 3):
  print(*combi)
for perm in permutations(range(1, n+1)):
  print(*perm)