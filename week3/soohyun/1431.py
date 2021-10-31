# 백준 1431 시리얼 번호
n = int(input())
serial = [input() for _ in range(n)]

# 숫자 합 구하는 메서드
def s_num(x):
	result = [int(n) for n in x if n.isdigit()]
	return sum(result)

serial.sort(key=lambda x : (len(x), s_num(x), x)) # 갈이 -> 숫자 합 -> 사전 순으로 정렬

for s in serial:
	print(s)