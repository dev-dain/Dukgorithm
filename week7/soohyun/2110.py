# 백준 2110 공유기 설치
N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort() # 오름차순 정렬
low, high = 1, house[-1] - house[0]

# 이분탐색 수행
while low <= high:
    mid = (low + high) // 2
    cur = house[0] # 공유기를 설치한 마지막 위치
    count = 1 # 설치한 공유기 개수

		# 앞 집부터 공유기 설치
    for i in range(1, N):
        if house[i] >= cur + mid:
            cur = house[i]
            count += 1

    if count >= C:
        low = mid + 1
    else:
        high = mid - 1

print(high)