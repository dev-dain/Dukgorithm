# 09-03
from itertools import combinations

while True:
  n, *lotto = input().split()
  if int(n) == 0:
    break
  for combi in combinations(lotto, 6):
    print(' '.join(combi))
  print()