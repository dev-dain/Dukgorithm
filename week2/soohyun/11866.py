# 백준 11866 요세푸스 문제 0
n, k = map(int, input().split())
people = [i for i in range(1, n+1)]

idx = 0 # 제거해야 할 위치 
delete = [] # 제거할 순서를 담은 리스트

while people:
	idx = (idx + k - 1) % len(people) # 제거할 위치 구하기
	delete.append(people.pop(idx))
print('<' + str(delete)[1: -1] + '>')