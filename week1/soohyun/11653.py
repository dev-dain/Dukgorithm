# 백준 11653 소인수분해
n = int(input())
divide = 2 # 나눌 숫자

while n > 1: # 더 이상 나눌 수 없을 때까지 반복
	if n % divide == 0: # 나눌 수 있다면 소인수분해
		n = n / divide
		print(divide)
	else: # 나눌 수 없다면 나눌 숫자 갱신
		divide += 1