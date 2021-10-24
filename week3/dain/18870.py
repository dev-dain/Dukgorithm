# 10-14
import sys
input = sys.stdin.readline

input()
arr = list(map(int, input().split()))
# set으로 만든 다음 딕셔너리로 원래 값: 새 값을 만들어주기
new_arr = sorted(list(set(arr)))
dic = {new_arr[i] : i for i in range(len(new_arr))}
for i in arr:
  print(dic[i], end=' ')