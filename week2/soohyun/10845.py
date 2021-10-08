# 백준 10845 큐
import sys

n = int(sys.stdin.readline())
queue = []

for _ in range(n):
	cmd = sys.stdin.readline().split()

	if cmd[0] == 'push':
		queue.append(cmd[1])
	elif cmd[0] == 'pop':
		if queue:
			print(queue.pop(0))
		else:
			print(-1)
	elif cmd[0] == 'size':
		print(len(queue))
	elif cmd[0] == 'empty':
		print(int(not queue))
	elif cmd[0] == 'front':
		if queue:
			print(queue[0])
		else:
			print(-1)
	elif cmd[0] == 'back':
		if queue:
			print(queue[-1])
		else:
			print(-1)