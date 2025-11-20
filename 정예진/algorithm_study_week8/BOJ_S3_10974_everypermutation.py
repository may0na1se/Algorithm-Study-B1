# 접근 방법 : 평범한 순열 뽑기 문제, 재귀 연습하는 문제

import sys

N = int(sys.stdin.readline())

path = [0] * N
visited = [0] * (N+1)


def recur(cnt):
    if cnt == N:
        print(*path)
        return

    for i in range(1, N+1):
        if visited[i]:
            continue

        visited[i] = 1
        path[cnt] = i
        recur(cnt+1)
        visited[i] = 0

recur(0)