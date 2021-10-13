n = int(input())
n_list = list(map(int, input().split()))

# set 중복 제거를 위해
for i in sorted(list(set(n_list))):
    print(i, end = ' ')