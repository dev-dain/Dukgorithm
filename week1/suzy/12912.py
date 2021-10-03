a, b = map(int, input().split())
if a == b:
    print(a)
else:
    print(((max(a,b)-min(a,b)+1)*(a+b))//2)