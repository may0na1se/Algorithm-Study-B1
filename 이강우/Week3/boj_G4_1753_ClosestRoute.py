'''
문제: https://www.acmicpc.net/problem/1753
접근: 그냥 다익스트라처럼 풀었음

시간복잡도: 다익스트라니까 O(VlogE) 아마도
'''

import sys
from heapq import heappush, heappop

V, E = map(int, input().split())
K = int(input())

edges = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    edges[u].append((w, v))

visited = [21e8] * (V+1)
visited[K] = 0

pq = [(0, K)]

while pq:
    cur_cost, cur_node = heappop(pq)

    for next_cost, next_node in edges[cur_node]:
        if visited[next_node] <= next_cost + cur_cost:
            continue
        visited[next_node] = next_cost + cur_cost
        heappush(pq, (next_cost + cur_cost, next_node))

for i in range(1, V+1):
    if visited[i] == 21e8:
        print('INF')
    else:
        print(visited[i])