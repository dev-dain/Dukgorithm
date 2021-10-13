# 백준 11586 지영 공주님의 마법 거울
n = int(input())
mirror = [input() for _ in range(n)]
state = int(input())

if state == 1:
	for m in mirror: print(m)
elif state == 2:
	for m in mirror: print(m[::-1])
elif state == 3:
	for m in mirror[::-1]: print(m)