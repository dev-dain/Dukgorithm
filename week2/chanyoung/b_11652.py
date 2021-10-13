##첫번째 풀이가 틀린 이유 : 조건을 만족하지 못함.(작은 수를 출력해야함)
#sol. dictionary를 사용함.
import sys

N = int(input())
my_dict = {}
for i in range(N):
   num = int(sys.stdin.readline())
   if num not in my_dict.keys():
      my_dict[num] = 1
   else:
      my_dict[num] = my_dict[num] + 1
max_num = max(list(my_dict.values()))
answer = []
for key, value in my_dict.items():
    if value == max_num:
               answer.append(key)
print(min(answer))
