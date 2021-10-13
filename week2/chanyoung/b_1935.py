n=int(input())
s = input()
stack = []
L = [int(input()) for i in range(n)]
for i in s:
    if 'A' <= i <='Z':
        stack.append(L[ord(i)-65])
    else:
        a = stack.pop()
        b = stack.pop()
        if i == '+':
            stack.append(a+b)
        elif i == '-':
            stack.append(b-a)
        elif i == '/':
            stack.append(b/a)
        elif i == '*':
            stack.append(a*b)
print("%.2f" % (stack[0]))
