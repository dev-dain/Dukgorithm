# 백준 17087 숨바꼭질 6
n, S = map(int, input().split())
pos = list(map(int, input().split()))
dif = list(set(abs(p - S) for p in pos)) # 수빈이와 동생들의 위치 차이 리스트
D = min(dif)

# 최대공약수 구하는 메서드
def gcd(a, b):
	res = 0
	while b:
		res = a % b
		a = b
		b = res
	return a

# 모든 동생들을 찾기 위한 D의 최대값 구하기
for d in dif:
	D = gcd(d, D)
print(D)