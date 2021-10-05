# 주어진 범위의 모든 소수를 에라스토테네스의 체를 이용하여 구하기
import math

# test case 개수
n = int(input())

# 0과 1는 소수가 아니라 False 나머진 True
prime_list = [0, 0] + [1] * 9999

# 2 부터 n의 제곱근까지 루프
for i in range(2, int(math.sqrt(10000)) + 1):
    # 만약 해당 index True , 소수라면
    if prime_list[i]:
        # 소수 배수들은 모두 False가 되어야함
        for j in range(i * 2, len(prime_list), i):
            prime_list[j] = 0

for i in range(n):
    number = int(input())
    i = 0
    # n//2 부터 소수의 차이가 가장 작은 값을 구한다
    while True:
        if prime_list[number // 2 - i] and prime_list[number // 2 + i]:
            print(number // 2 - i, number // 2 + i)
            break
        else:
            i += 1