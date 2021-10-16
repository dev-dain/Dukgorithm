n=int(input())
N=list(map(int, input().split()))
T=[]

for i in range (0,n): #0~N-1까지
   t=[]
   for j in range(0,n):
        if(N[i]>N[j]) :
           t.append(N[j])
   t=set(t)
   T.append(len(t))

print(*T)
