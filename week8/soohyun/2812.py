# 백준 2812 크게 만들기
N, K = map(int, input().split())
nums = list(input())
k, stack = K, []

for i in range(N):
    while k > 0 and stack and stack[-1] < nums[i]: # 앞에 숫자가 뒤의 숫자보다 작을 경우 지운다
        stack.pop()
        k -= 1
    stack.append(nums[i])
print(''.join(stack[:N-K])) # K개를 지우지 못하는 경우를 위해 인덱스 슬라이싱을 해준다