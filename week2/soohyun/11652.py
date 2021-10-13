# 백준 11652 카드
n = int(input())
cards = {}
for _ in range(n):
	c = int(input())
    # 키 값 체크 후 카드개수 업데이트
	if c in cards: cards[c] += 1
	else: cards[c] = 1
	
cards = sorted(cards.items(), key=lambda x: (-x[1], x[0])) # 카드개수 내림차순 -> 카드값 오름차순 정렬
print(cards[0][0])