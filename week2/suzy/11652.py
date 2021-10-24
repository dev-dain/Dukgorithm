n = int(input())

card_dict = dict()

# key 정수값, value 빈도수 저장
for _ in range(n):
    card = int(input())
    if card in card_dict:
        card_dict[card] += 1
    else:
        card_dict[card] = 1
# 최다 빈도수를 가진 정수를 제일 앞으로
# 최다 빈도 정수가 여러개일 경우 작은 것 먼저
print(sorted(card_dict.items(), key=lambda x: (-x[1], x[0]))[0][0])
