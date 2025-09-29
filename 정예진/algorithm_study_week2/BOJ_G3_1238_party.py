import sys
from heapq import heappop, heappush

N, M, X = map(int, sys.stdin.readline().split())

roads_to_x = [[] for _ in range(N+2)]
roads_to_home = [[] for _ in range(N+2)]

for _ in range(M):
    s, e, d = map(int, sys.stdin.readline().split())
    roads_to_x[s].append((d, e))
    roads_to_home[e].append((d, s))


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