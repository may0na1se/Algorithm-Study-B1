# boj 1920 수 찾기
# set을 쓰는게 가장 간단할 듯
# 이진 탐색으로도 해결 가능


N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
B = list(map(int, input().split()))
for b in B:
    start, end = 0, N - 1
    while start <= end:
        C = (start + end) // 2
        if A[C] == b:
            print(1)
            break
        elif A[C] > b:
            end = C - 1
        else:
            start = C + 1
    else:
        print(0)