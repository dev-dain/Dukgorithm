# 백준 11650 좌표 정렬하기
import sys

n = int(sys.stdin.readline())
dot = [] # 점 리스트

for _ in range(n):
	x, y = map(int, sys.stdin.readline().split())
	dot.append([x, y])

dot.sort() # x좌표 -> y좌표 순으로 오름차순 정렬

for d in dot:
	print(d[0], d[1])