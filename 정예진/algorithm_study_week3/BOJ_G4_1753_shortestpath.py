# 접근 방법: 사실 그냥 다익스트라 구현 문제입니다
# 오답 났던 이유는.. 출력이 INF로 안 나오고 소문자로 나와서..
# 걸린 시간 : 20분

import sys
from heapq import heappop, heappush

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] * (V+1) for _ in range(V+1)]
INF = float('inf')

for _ in range(E):
    s,e,w = map(int, sys.stdin.readline().split())
    graph[s].append((w,e))


def dijkstra(start):
    dist = [INF] * (V+1)
    dist[start] = 0

    pq = [(0, start)]
    while pq:
        d, now = heappop(pq)

        if d > dist[now]:
            continue

        for next_dist, next_node in graph[now]:
            if dist[next_node] > d + next_dist:
                dist[next_node] = d + next_dist
                heappush(pq, (dist[next_node], next_node))
    return dist


dist = dijkstra(start)

for idx in range(1, len(dist)):
    if dist[idx] == INF:
        print("INF")
    else:
        print(dist[idx])

