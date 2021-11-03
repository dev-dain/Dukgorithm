# dp
# 초기값
zero = [1,0,1]
one = [0,1,1]

def fib(n):
    length = len(zero)
    if length <= n:
        for i in range(length, n+1):
            # 0 과 1 호출 횟수 역시 피보나치 점화식
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print("%d %d" %(zero[n], one[n]))

# testcase t
t = int(input())
for i in range(t):
    i = int(input())
    fib(i)