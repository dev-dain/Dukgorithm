n = int(input())

for _ in range(n):
    t = input()
    vps = []

    for i in t:
        if i == '(':
            vps.append(i)

        elif i == ')':
            # 스텍에 ( 가 존재하는 경우
            if len(vps) != 0 and vps[-1]=='(':
                vps.pop()
            # 스텍이 빈경우
            else:
                vps.append(i)
                break
    # 괄호의 갯수가 일치한다면
    if len(vps) == 0:
        print("YES")
    else:
        print("NO")