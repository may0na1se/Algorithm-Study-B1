'''
문제: https://www.acmicpc.net/problem/1916
접근: 기억 X

시간복잡도: 미안해
'''

import sys
from heapq import heappush, heappop

def func(d, cost):
    pq = [(d, cost)]

    visited = [21e8] * (N + 1)
    visited[start] = 0

    while pq:
        now, total = heappop(pq)
        if total >= visited[end]:
            continue
        for next, fee in buses[now]:
            if total + fee >= visited[next]:
                continue
            visited[next] = total + fee
            heappush(pq, (next, total + fee))
    return visited[end]


N = int(input())
towns = [0] * (N + 1)

M = int(input())
buses = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, c = map(int, sys.stdin.readline().split())
    heappush(buses[s], (e, c))

start, end = map(int, input().split())

print(func(start, 0))
