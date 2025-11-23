import sys
input = sys.stdin.readline

# sys.stdin = open('input.txt', 'r')


N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((w,e))
    graph[e].append((w,s))

# print(graph)

from heapq import heappop, heappush

n1, n2 = map(int, input().split())

# 1 -> n1 -> n2 -> N
# 1 -> n2 -> n1 -> N   
#1, n1, N에서 다익스트라를 하면 되지 않을까? n1->n2와 n2->n1은 같으니까

INF = 10**8
dist = [INF] * (N+1)

start = 1
dist[start] = 0

pq = [(dist[start], start)]

while pq:
    cur_dist, cur_node = heappop(pq)
    # print(cur_dist, cur_node)
    if dist[cur_node] < cur_dist:
        continue

    for next_dist, next_node in graph[cur_node]:
        new_dist = cur_dist + next_dist
        if new_dist < dist[next_node]:
            dist[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

# print(dist)

start_to_n1, start_to_n2 = dist[n1], dist[n2]

#n1에서 다익스트라

dist = [INF] * (N+1)
start = n1
dist[start] = 0
pq = [(dist[start], start)]

while pq:
    cur_dist, cur_node = heappop(pq)
    # print(cur_dist, cur_node)
    if dist[cur_node] < cur_dist:
        continue

    for next_dist, next_node in graph[cur_node]:
        new_dist = cur_dist + next_dist
        if new_dist < dist[next_node]:
            dist[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

# print(dist)
n1_to_n2 = dist[n2]

#N에서 다익스트라

dist = [INF] * (N+1)
start = N
dist[start] = 0
pq = [(dist[start], start)]

while pq:
    cur_dist, cur_node = heappop(pq)
    # print(cur_dist, cur_node)
    if dist[cur_node] < cur_dist:
        continue

    for next_dist, next_node in graph[cur_node]:
        new_dist = cur_dist + next_dist
        if new_dist < dist[next_node]:
            dist[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

# print(dist)

N_to_n1, N_to_n2 = dist[n1], dist[n2]

#1->n1->n2->N 거리  vs  1->n2->n1->N 비교

# print(start_to_n1 + n1_to_n2 + N_to_n2,  start_to_n2 + n1_to_n2 + N_to_n1)

if min(start_to_n1 + n1_to_n2 + N_to_n2,  start_to_n2 + n1_to_n2 + N_to_n1) >= INF:
    print(-1)
else:
    print(min(start_to_n1 + n1_to_n2 + N_to_n2,  start_to_n2 + n1_to_n2 + N_to_n1))