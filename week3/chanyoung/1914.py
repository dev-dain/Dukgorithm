N = int(input()) 
def HANOI(x, y, z, cnt):
    if cnt == 0:
        return 
    HANOI(x, z, y, cnt - 1) 
    print(x,z) 
    HANOI(y, x, z, cnt - 1) 
print((1 << N) - 1) 
if N <= 20: 
    HANOI(1, 2, 3, N)
