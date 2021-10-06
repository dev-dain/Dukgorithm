#백준 11650
#좌표 정렬하기
#### 못풀어서 풀이 참고함.

import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort(key=lambda x : (x[0], x[1]))
for e in lst:
  print(e[0], e[1])