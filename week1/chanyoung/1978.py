#백준 1978 
#소수구하기
n=int(input())
nlist = list(map(int,input().split()))

cnt = 0 

for i in nlist :
    if i == 1 : continue    #1은 약수가 아니므로
    for k in range (2, int(i**0.5)+1):
        if i % k == 0 : break
    else : cnt+=1

print(cnt)