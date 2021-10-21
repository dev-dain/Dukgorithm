# 백준 1914 하노이 탑
n = int(input())
def hanoi(n, p_from, p_mid, p_to):
	if n == 1: # 원반이 하나 남은 경우 무조건 1번 기둥에서 3번 기둥으로 이동
		print(p_from, p_to)
		return

	hanoi(n-1, p_from, p_to, p_mid) # 1번 기둥의 n-1개 원반을 2번 기둥으로 이동
	print(p_from, p_to) # 1번 기둥의 가장 큰 원반을 3번 기둥으로 이동
	hanoi(n-1, p_mid, p_from, p_to) # 2번 기둥의 n-1개 원반을 3번 기둥으로 이동

print(2 ** n - 1) # 이동 횟수
if n <= 20: hanoi(n, 1, 2, 3)	