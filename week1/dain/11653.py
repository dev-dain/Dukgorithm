# 08-14
def solution(n):
  org_n = n
  if n == 1: return

  for i in range(2, int(n**1/2)+1):
    while n % i == 0:
      print(i)
      n //= i
  if org_n == n: print(n)

n = int(input())
solution(n)


# for를 안 쓰고 while만으로도 쓸 수 있음
# https://www.acmicpc.net/source/32178286
# 굿 코드..
# d = 2
# while d <= n:
#     if n % d == 0:
#         print(d)
#         n /= d
#     else:
#         d += 1