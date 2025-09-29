import sys
from heapq import heappop, heappush

N, M = map(int, sys.stdin.readline().split())
roads = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, d = map(int, sys.stdin.readline().split())
    roads[s].append((d, e))
    roads[e].append((d, s))

max_dist = 0
total_dist = 0
cnt = 1
visited = [0] * (N+1)

start = 1
visited[start] = 1
road_can = []
for dist, end in roads[start]:
    heappush(road_can, (dist, end))

while cnt < N:
    next_d, next_e = heappop(road_can)
    if visited[next_e]:
        continue

    max_dist = max(max_dist, next_d)
    total_dist += next_d
    visited[next_e] = 1
    cnt += 1
    start = next_e

    for dist, end in roads[start]:
        if visited[end]:
            continue
        heappush(road_can, (dist, end))


print(total_dist-max_dist)