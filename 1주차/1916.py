import sys
import math
import heapq

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    result[s] = 0
    while q:
        distance, now = heapq.heappop(q)
        if result[now] < distance:
            continue
        for i in graph[now]:
            if distance + i[1] < result[i[0]]:
                result[i[0]] = distance + i[1]
                heapq.heappush(q, (distance + i[1], i[0]))

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
result = [math.inf] * (N + 1)
visited = [0] * (N + 1)
for _ in range(M):
    a, b, cost = map(int, sys.stdin.readline().split())
    graph[a].append((b, cost))
start, goal = map(int, input().split())

dijkstra(start)
print(result[goal])