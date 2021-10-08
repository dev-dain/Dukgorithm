# 10-07
n = int(input())
s = input()
alphabet = {}
for i in range(n):
  alphabet[chr(65+i)] = int(input())

stack = []
for c in s:
  if c.isupper():
    stack.append(alphabet[c])
  else:
    if c == '*':
      stack.append(stack.pop() * stack.pop())
    elif c == '+':
      stack.append(stack.pop() + stack.pop())
    else:
      x2 = stack.pop()
      x1 = stack.pop()
      if c == '/':
        stack.append(x1 / x2)
      else:
        stack.append(x1 - x2)
print('{:.2f}'.format(stack[0]))