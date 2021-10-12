import sys
n=int(input())
str=input()
nums=[0]*n
for i in range(n):
    nums[i]=int(input())
stack=[]

for ch in str:
    if ch.isupper():
        stack.append(nums[ord(ch)-ord('A')])
    else:
        num2=stack.pop()
        num1=stack.pop()
        if ch=='+':
            stack.append(num1+num2)
        elif ch=='-':
            stack.append(num1-num2)
        elif ch=='/':
            stack.append(num1/num2)
        elif ch=='*':
            stack.append(num1*num2)
print(f"{stack[0]:.2f}")
