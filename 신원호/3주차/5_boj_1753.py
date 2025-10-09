import sys
import heapq

# 시작 지점으로부터 모든 노드로의 최단 거리 계산
def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    result[s] = 0
    while q:
        distance, now = heapq.heappop(q)
        if result[now] < distance:
            continue
        for i in graph[now]:
            if distance + i[0] < result[i[1]]:
                result[i[1]] = distance + i[0]
                heapq.heappush(q, (distance + i[0], i[1]))

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((w, v))

result = [300000000] * (V + 1)
dijkstra(start)
for n in range(1, V + 1):
    if result[n] == 300000000:
        print('INF')
    else:
        print(result[n])