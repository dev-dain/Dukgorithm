# (틀렸음) 왤까? int(x**1/2)+1, 1, -1이던 것을 고쳤더니 됨
# 08-12
# 소수 찾기
input()
l = list(map(int, input().split()))
cnt = 0

for x in l:
  if x <= 1: continue
  for j in range(2, int(x ** 1/2)+1):
    if x % j == 0: break
  else:
    cnt += 1

print(cnt)