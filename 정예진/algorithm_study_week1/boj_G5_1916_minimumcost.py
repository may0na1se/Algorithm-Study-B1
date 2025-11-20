import sys
from heapq import heappop, heappush
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

buses = [[] for _ in range(N+1)]

for _ in range(M):
    s,e,c = map(int, sys.stdin.readline().split())
    buses[s].append((e,c))

S, E = map(int, sys.stdin.readline().split())

def dijkstra(start_node):
    pq = [(start_node, 0)]
    dists = [float("INF")] * (N+1)
    dists[start_node] = 0

    while pq:
        node, dist = heappop(pq)

        if dists[node] < dist:
            continue

        for next_node, next_dist in buses[node]:
            new_dist = dist + next_dist

            if dists[next_node] <= new_dist:
                continue

            dists[next_node] = new_dist
            heappush(pq, (next_node, new_dist))

    return dists

result = dijkstra(S)

print(result[E])