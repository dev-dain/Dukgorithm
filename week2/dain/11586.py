n = int(input())
mirror = [list(input()) for _ in range(n)]
k = int(input())

for i in range(len(mirror)):
  if k == 1:  # 있는 그대로 join
    print(''.join(mirror[i]))
  elif k == 2:  # 좌우 반전 (reverse)
    print(''.join(reversed(mirror[i])))
  else: # 상하 반전을 위해 음수부터 거꾸로 함
    print(''.join(mirror[-i-1]))