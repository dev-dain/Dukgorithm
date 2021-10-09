# 08-19
from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
# 예제에서 빈도수가 똑같으면 더 작은 수가 나오기 때문에 sorted 필요
cards = Counter(sorted([int(input()) for _ in range(n)]))
print(cards.most_common(1)[0][0]) # Counter의 most_common을 사용해 풀이 가능