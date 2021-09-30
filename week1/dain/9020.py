# 08-25
table = [0, 0] + [1] * 9999
for i in range(len(table)):
  if table[i]:
    for j in range(i*2, len(table), i):
      table[j] = 0

t = int(input())
for _ in range(t):
  n = int(input())
  divide = []
  
  for i in range(2, (n//2)+1):
    if table[i] and table[n-i]:
      divide.append([i, n-i, abs(n-i)])
  divide.sort(key=lambda x: x[2])

  print('{} {}'.format(divide[0][0], divide[0][1]))