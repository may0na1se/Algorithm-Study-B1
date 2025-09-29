import sys
import heapq

def dijkstra(s, g):
    q = []
    heapq.heappush(q, (0, s))
    result[s] = 0
    while q:
        distance, now = heapq.heappop(q)
        if now == g:
            return distance
        if result[now] < distance:
            continue
        for i in graph[now]:
            if distance + i[1] < result[i[0]]:
                result[i[0]] = distance + i[1]
                heapq.heappush(q, (distance + i[1], i[0]))

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
result = [float('inf')] * (N + 1)
for _ in range(M):
    a, b, cost = map(int, sys.stdin.readline().split())
    graph[a].append((b, cost))
start, goal = map(int, input().split())

print(dijkstra(start, goal))
