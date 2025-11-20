# 접근방법 : 사실 원호오빠가 지난주에 이 문제 설명하는 걸 들어버렸습니다
# 다익스트라, 집 -> 파티장 -> 집을 오가는 걸 표현하기 위해 주어진 방향과 반대되는 그래프 1개 더 만듦
# 각 그래프에 대해 파티장 -> 집까지의 최소 거리를 구해 이를 각각 더해 가장 오래 걸리는 집 고르기

import sys
from heapq import heappop, heappush

N, M, X = map(int, sys.stdin.readline().split())

roads_to_x = [[] for _ in range(N+2)]
roads_to_home = [[] for _ in range(N+2)]

for _ in range(M):
    s, e, d = map(int, sys.stdin.readline().split())
    roads_to_x[s].append((d,e))
    roads_to_home[e].append((d,s))


def dijkstra(start, roads):
    pq = [(0, start)]
    dists = [21e8] * (N+1)
    dists[start] = 0

    while pq:
        dist, e = heappop(pq)
        if dists[e] < dist:
            continue

        for next_d, next_e in roads[e]:
            new_d = dist + next_d

            if dists[next_e] < new_d:
                continue

            dists[next_e] = new_d
            heappush(pq, (new_d, next_e))

    return dists

road1 = dijkstra(X, roads_to_x)
road2 = dijkstra(X, roads_to_home)

max_dist = 0
for idx in range(1, N+1):
    n_dist = road1[idx] + road2[idx]
    if max_dist < n_dist:
        max_dist = n_dist

print(max_dist)