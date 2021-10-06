#백준 9020
#골드바흐의 추측

def prime_num():
    num = []
    n = 10000
    num_range = [True]*(n+1)
    num_range[0] = False
    num_range[1] = False
    
    for i in range(n+1):
        if num_range[i]:
            num.append(i)
            for j in range(2*i,n+1,i):
                num_range[j] = False
    return num

prime = prime_num()

def sol(n):
    i = n//2
    j = n//2
    for x in range(i,n):
        if (x in prime) and (j in prime):
            print(j,x)
            break
        j -= 1
        
test_case = int(input())

for i in range(test_case):
    n = int(input())
    sol(n)