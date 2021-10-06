# 통과 못했음 ..
import math

n = int(input())
nums = list(map(int, input().split()))

# 소수의 개수
cnt = 0
for i in nums:
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            break
        else:
            print(i)
            cnt += 1
print(cnt)

