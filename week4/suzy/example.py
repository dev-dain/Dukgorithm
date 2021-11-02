def climbStairs(n: int) -> int:
    c = [0]*(n+1)
    c[0] = 1
    c[1] = 2
    print(c)

    if n < 3:
        return c[n-1]

    for i in range(2,n):
        c[i] = c[i-1] + c[i-2]
        print(c)
    return c[n-1]

print(climbStairs(3))