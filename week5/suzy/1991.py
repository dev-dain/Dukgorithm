from collections import defaultdict
# 이진 트리의 노드 개수
n = int(input())

# {'A' : ['B','C'], ... }
tree = defaultdict(list)
for i in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]


# 전위 root left right
def fnt(root):
    if root != '.':
        print(root, end='') # root
        fnt(tree[root][0]) # left
        fnt(tree[root][1]) # right

# 중위
def mid(root):
    if root != '.':
        mid(tree[root][0]) # left
        print(root, end='') # root
        mid(tree[root][1]) # right

# 후위
def last(root):
    if root != '.':
        last(tree[root][0]) # left
        last(tree[root][1]) # right
        print(root, end='') # root

fnt('A')
print()
mid('A')
print()
last('A')

