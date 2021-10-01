# 백준 1978 소수찾기
n = int(input())
nums = list(map(int, input().split()))
count = 0

for num in nums:
	if num > 1: # 1은 소수가 아니므로 제외
    # 소수인지 판별
		for i in range(2, int(num ** 0.5)+1):
			if num % i == 0: # 나눠지는 값이 있다면 소수가 아니므로 break
				break
		else: # 소수인 경우
			count += 1
print(count)