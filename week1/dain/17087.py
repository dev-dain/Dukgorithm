# 10-01
import sys, math
input = sys.stdin.readline
n, s = map(int, input().split())
a = list(map(int, input().split()))
a = [abs(s-x) for x in a]
print(math.gcd(*a))