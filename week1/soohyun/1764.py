# 백준 1764 듣보잡
n, m = map(int, input().split())

not_listen = [input() for _ in range(n)]
not_look = [input() for _ in range(m)]

# 듣보잡 구한 후  사전 순으로 정렬
result = list(set(not_listen) & set(not_look))
result.sort()

print(len(result))
for r in result:
	print(r)