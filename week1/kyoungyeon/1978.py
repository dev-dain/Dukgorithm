# no.1978 소수 찾기
num_count = int(input(""))
num_list = list(map(int, input().split(' ')))
count = 0

if len(num_list) == num_count:
    for i in num_list:
        if i == 1:
            continue
        if i == 2:
            count += 1
            continue
        for j in range(2, i, 1):
            if i % j == 0:
                break
        else:
            count += 1

print(count)