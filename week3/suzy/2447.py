import sys

def Star(n):
    if n == 1:
        return ['*']

    Stars = Star(n//3)
    l = []
    # ***
    for _ in Stars:
        l.append(_*3)
    # * *
    for _ in Stars:
        l.append(_+' '*(n//3)+_)
    # ***
    for _ in Stars:
        l.append(_*3)
    return l

n = int(sys.stdin.readline())
print('\n'.join(Star(n)))