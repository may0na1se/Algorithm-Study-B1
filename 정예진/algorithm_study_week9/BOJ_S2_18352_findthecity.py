import sys
from heapq import heappop, heappush

input = sys.stdin.readlines()

N, M, K, X = map(int, input[0].strip().split())
city = [[] for _ in range(N+1)]

for _ in range(1, M+1):
    s, e = map(int, input[_].strip().split())
    city[s].append(e)

def dijkstra(start):
    pq = [(0, start)]
    dists = [float('INF')] * (N+1)
    dists[start] = 0

    while pq:
        dist, node = heappop(pq)

        if dists[node] < dist:
            continue

        for n_node in city[node]:
            new_dist = dist + 1
            if dists[n_node] <= new_dist:
                continue
            dists[n_node] = new_dist
            heappush(pq, (new_dist, n_node))
    return dists

result = dijkstra(X)
target = []
for idx in range(1,N+1):
    if result[idx] == K:
        target.append(idx)

if target:
    for i in range(len(target)):
        print(target[i])
else:
    print(-1)