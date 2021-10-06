#백준 1182
#부분수열의 합

##못풀어서 풀이 참고함.
#지난 시간에 배웠던 Itertools의 combinations를 사용할 생각을 못했음. 더 연습해야함

from itertools import combinations

n, s = map (int, input().split())
arr=list(map(int, input().split()))
cnt=0

for i in range(1, n+1):
    for combi in combinations(arr, i):
        if sum(combi)==s:
            cnt+=1

print(cnt)