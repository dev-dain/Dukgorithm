# 백준 9012 괄호
n = int(input())

for _ in range(n):
	data = input()
	stack = []

	for d in data:
		if d == '(':
			stack.append('(')
		elif d == ')':
			if len(stack) != 0 and stack[-1] == '(':
				stack.pop()
			else:
				stack.append(')')
				break

	if len(stack) == 0: print('YES')
	else: print('NO')