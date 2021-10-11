n = int(input())

for _ in range(n):
    t = input()
    # 각 괄호를 하나씩 리스트로 저장
    tt = list(t)
    cnt = 0

    for i in tt:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1

        if cnt < 0:
            print("NO")
            break

    # 안쪽괄호 바깥쪽괄호 수가 같다면 0
    if cnt == 0:
        print("YES")
    elif cnt>0:
        print("NO")
