n = int(input())
li = list(map(int, input().split()))

# set 중복 제거
for i in sorted(list(set(li))):
    print(i, end = ' ')