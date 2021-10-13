#첫번째 풀이 -> 시간초과로 틀림

import sys
from collections import deque

queue = deque()

def push(a):
    queue.append(a)

def pop():
    if(not queue):
        return -1
    else:
        return queue.popleft()

def size():
    return len(queue)

def empty():
    if queue:
        return 0
    else:
        return 1

def front():
    return queue[0] if queue else -1

def back():
    return queue[-1] if queue else -1

stack = []
n = int(input())

for i in range(n):
    
    command = sys.stdin.readline().rstrip().split()
    
    a1 = command[0]

    if a1 == "push":
        push(command[1])
    elif a1 == "pop":
        print(pop())
    elif a1 == "size":
        print(size())
    elif a1 == "empty":
        print(empty())
    elif a1 == "front":
        print(front())
    elif a1 == "back":
        print(back())
