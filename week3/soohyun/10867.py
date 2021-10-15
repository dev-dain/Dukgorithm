# 백준 10867 중복 빼고 정렬하기
n = int(input())
nums = list(set(map(int, input().split()))) # 중복 제거
nums.sort() # 오름차순 정렬
print(*nums)