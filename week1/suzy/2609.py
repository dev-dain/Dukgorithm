def gcd(a, b):
    a, b = max(a,b), min(a,b)
    res = 0
    while b:
        res = a % b
        a = b
        b = res
    return a

def lcm(a,b):
    return(a*b)//gcd(a,b)

a,b = map(int, input().split())
print(gcd(a,b))
print(lcm(a,b))