'''
문제: https://www.acmicpc.net/problem/1916
접근: 단방향 그래프 -> 출발지, 도착지 비용 정보 넣고
dijkstra로 출발지점에서 목표 지점에 갈 수 있는 최소 비용 찾기
중간에 기존 경로의 비용보다 더 큰 비용이 들어오면 return

시간복잡도: O((V+E)logV) 라고 하는 구나~~
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
