# 백준 1003 피보나치 함수
t = int(input())

for _ in range(t):
	n = int(input())
	zero = [1, 0] + [0] * (n-1)
	one = [0, 1] + [0] * (n-1)

	if n <= 1:
		print(zero[n], one[n])
	else:
		for i in range(2, n+1):
			zero[i] = zero[i-1] + zero[i-2]
			one[i] = one[i-1] + one[i-2]
		print(zero[n], one[n])