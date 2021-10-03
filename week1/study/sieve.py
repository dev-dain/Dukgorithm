import math
def sieve(n):
  # 0, 1은 어차피 소수가 아니므로 False. 나머지는 일단 True로 만듦
  prime = [0, 0] + ([1] * (n-1))
  # 2부터 n의 제곱근까지 루프 돌기
  for i in range(2, int(math.sqrt(n))+1):
    # 만약 해당 인덱스가 True, 즉 소수라면
    if prime[i]:
      # 소수의 배수들은 모두 False가 되어야 함
      for j in range(i*2, len(prime), i):
        prime[j] = 0
  # 이대로 하면 [0, 0, 1, 1, 0, 1] 이런 식이기 때문에 enumerate로 정리해줌
  return [idx for idx, val in enumerate(prime) if val]
print(sieve(997))