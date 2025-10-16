N = int(input())

M = int(input())

import heapq


graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, cost = map(int, input().split())
    graph[s].append((cost, e))

start, end = map(int, input().split())
pq = [(0, start)]

INF = 10**8
dist = [INF] * (N+1)
dist[start] = 0


# print(graph)

while pq:
    cur_cost, cur_node = heapq.heappop(pq)
 #   if cur_cost > dist[cur_node]:
  #      continue
    if cur_node == end :
        break
        
    for cost, next_node in graph[cur_node]:
        new_cost = cost + cur_cost
        if new_cost < dist[next_node]:
            dist[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))


print(dist[end])