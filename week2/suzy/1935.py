n = int(input())
exp = list(input())
nums = [int(input()) for _ in range(n)]

ans = []

for i in exp:
    # 만약 문자인 경우 ord() > 아스키 코드값으로 변환 후 배열 인덱스를 구해 추가
    if 'A' <= i <= 'Z':
        ans.append(nums[ord(i) - ord('A')])
    else:
        x = ans.pop()
        y = ans.pop()
        if i == '+':
            ans.append(x+y)
        elif i == '-':
            ans.append(y-x)
        elif i == '*':
            ans.append(x*y)
        elif i == '/':
            ans.append(y/x)

print(format(*ans, ".2f"))
