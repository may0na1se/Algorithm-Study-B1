'''
문제: https://www.acmicpc.net/problem/1238
접근: 왕복 다익스트라, 1주차 문제 중 최소비용 구하기(1916)와 비슷함.
최소비용 구하는 방법을 그냥 왕복으로 적용해주면 된다.

시간복잡도: 일반 다익스트라가 O((V+E)logV) 라고 하니까. 그거의 2배?
'''

import sys
from heapq import heappop, heappush


def dijkstra(n):
    pq = [(0, n)]
    visited = [21e8] * (N+1)
    visited[n] = 0
    min_time = 21e8
    
    while pq:
        current_time, current_position = heappop(pq)
        if current_position == X:
            times[n] += current_time
            break

        for time_add, next_position in towns[current_position]:
            total = current_time + time_add
            if total >= min_time:
                continue
            if total >= visited[next_position]:
                continue
            visited[next_position] = total
            heappush(pq, (total, next_position))

    pq = [(0, X)]
    visited = [21e8] * (N+1)
    visited[X] = 0
    min_time = 21e8

    while pq:
        current_time, current_position = heappop(pq)
        if current_position == n:
            times[n] += current_time
            break

        for time_add, next_position in towns[current_position]:
            total = current_time + time_add
            if total >= min_time:
                continue
            if total >= visited[next_position]:
                continue
            visited[next_position] = total
            heappush(pq, (total, next_position))


N, M, X = map(int, input().split())

# 1번 마을부터 N번 마을 -> 인덱스 0은 무시
towns = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, t = map(int, sys.stdin.readline().split())
    heappush(towns[s], (t, e))

times = [0] * (N+1)

for i in range(1, N+1):
    dijkstra(i)


print(max(times))