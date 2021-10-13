from collections import deque

# 요세푸스 순열 (n 사람수, k 순서 제거)
n, k = map(int, input().split())
# range 사용
yo = deque(range(1, n+1))
ans = []

# k 번째 원소를 제거하기 위해
temp = k-1

while yo:
    # rotate 사용
    yo.rotate(-k)
    ans.append(str(yo.pop()))
print('<'+', '.join(map(str, ans))+'>')





