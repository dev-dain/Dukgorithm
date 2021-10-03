# 백준 9020 골드바흐의 추측
n = int(input())
prime = [0, 0] + [1] * 9999 # 소수 리스트

# 에라토스테네스의 체를 이용하여 소수 구하기
for i in range(2, int(10000 ** 0.5)+1):
	if prime[i]:
		for j in range(i*2, 10001, i):
			prime[j] = 0

# 두 소수의 차이가 가장 작은 골드바흐 파티션 구하기
for _ in range(n):
	num = int(input())
	idx = 0
	while True:
		if prime[num // 2 - idx] and prime[num // 2 + idx]:
			print(num // 2 - idx, num // 2 + idx)
			break
		idx += 1