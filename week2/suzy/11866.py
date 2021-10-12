from collections import deque

# 요세푸스 순열 (n 사람수, k 순서 제거)
n, k = map(int, input().split())
yo = deque()
ans = []

for i in range(n):
    yo.append(i+1)

# k 번째 원소를 제거하기 위해
temp = k-1

while yo:
    for i in range(k):
        if i == temp:
            p = yo.popleft()
            ans.append(p)
        else:
            p = yo.popleft()
            yo.append(p)

print('<'+', '.join(map(str, ans))+'>')





