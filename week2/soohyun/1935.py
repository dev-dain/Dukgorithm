# 백준 1935 후위표기식2
n = int(input())
postfix = input()
nums = [int(input()) for _ in range(n)]

stack = []
for p in postfix:
	if 'A' <= p <= 'Z': # 피연산자면 스택에 삽입
		stack.append(nums[ord(p) - ord('A')])
	else: # 연산자라면 스택에서 값을 가져와 계산한 후 스택에 삽입
		b = stack.pop()
		a = stack.pop()

		if p == '+': 
			stack.append(a + b)
		elif p == '-':
			stack.append(a - b)
		elif p == '*':
			stack.append(a * b)
		elif p == '/':
			stack.append(a / b)

print('%.2f' % stack[0])