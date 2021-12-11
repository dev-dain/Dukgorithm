# 백준 2448 별 찍기 - 11
N = int(input())
tri = ["  *  ", " * * ", "*****"]
N //= 3

def star():
    L = len(tri)
    for i in range(L):
        tri.append(tri[i] + ' ' + tri[i]) # 주어진 모양을 복사하여 아래쪽에 두개의 모양 만들기
        tri[i] =  ' ' * L + tri[i] + ' ' * L # 주어진 모양의 양쪽 여백 만들기

while N > 1:
    N //= 2
    star()

for t in tri:
    print(t)