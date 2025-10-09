import heapq
import sys
# sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

V, E = map(int, input().split())

INF = 10**8

start = int(input())


# visited = [0] * (V+1)

dist = [INF] * (V+1)

dist[start] = 0

graph = [[] for _ in range(V+1)]

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((e,w))

# print(graph)

pq = []

heapq.heappush(pq, (0, start))

while pq:
    current_dist, current_node = heapq.heappop(pq)
    if dist[current_node] < current_dist:
        continue
    
    # print(current_node)
    
    for node, d in graph[current_node]:
        # print(node)

        if dist[node] > current_dist + d:
            dist[node] = current_dist + d
            heapq.heappush(pq, (dist[node], node))   #heapq들어갈때는 (거리,목적지)
    # print(dist)

for _ in dist[1:]:
    if _ == INF:
        print("INF")
    else:
        print(_)
