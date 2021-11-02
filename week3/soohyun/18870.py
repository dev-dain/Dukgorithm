# 백준 18870 좌표 압축
n = int(input()) # 숫자의 개수
nums = list(map(int, input().split())) # 숫자 리스트

comp = sorted(list(set(nums))) # 중복 제거한 후 정렬
dic_comp = {comp[i] : i for i in range(len(comp))} # 딕셔너리로 변경

for num in nums:
	print(dic_comp[num], end = ' ') # 딕셔너리에서 인덱스 값을 찾아 출력