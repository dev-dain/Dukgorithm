import sys
n = int(sys.stdin.readline())

# n개의 시리얼 번호를 arr[] 저장
arr = [input() for _ in range(n)]

# 자리수 중 숫자인것들 더하기
def num_sum(x):
    result = [int(n) for n in x if n.isdigit()]
    return sum(result)

# 길이 다음은 합을 기준으로 정렬
arr.sort(key=lambda x: (len(x),num_sum(x),x))

for i in arr:
    print(i)