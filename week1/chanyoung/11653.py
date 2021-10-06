#백준 11653
#소인수분해

##이전 풀이는 while문을 사용하지 않은 풀이였는데, while문을 사용한 풀이로 참고하여 다시품
n=int(input())

for i in range(2, n+1):
    if(n%i==0) : 
        while(n%i==0):
            print(i)
            n=n/i