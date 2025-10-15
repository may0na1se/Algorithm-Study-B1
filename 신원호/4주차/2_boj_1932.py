# boj 1932 정수 삼각형
# dp

import sys
N = int(input())
tri = [[] for _ in range(N)]
for n in range(N):
    tri[n] = list(map(int, sys.stdin.readline().split()))
for i in range(1, N):
    for j in range(i + 1):
        # 오른쪽 사이드
        if j == i:
            tri[i][j] += tri[i - 1][-1]
        # 왼쪽 사이드
        elif j == 0:
            tri[i][j] += tri[i - 1][0]
        else:
            tri[i][j] += max(tri[i - 1][j - 1], tri[i - 1][j])
print(max(tri[N - 1]))