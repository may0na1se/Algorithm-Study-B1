'''
문제: https://www.acmicpc.net/problem/1504
접근: 특정 경로에 대한 최소 비용 = 다익스트라,
거쳐야 하는 두가지 정점이 있음 -> 목적지 다르게 설정해서 2번 돌려줌
나는 ㅂㅅ이다~~

시간복잡도: 다익스트라니까 O(VlogE * 2) 아마도
'''

import sys
from heapq import heappop, heappush

def dijkstra(s, e, cost):
    pq = [(cost, s)]
    temp = [0] * (N+1)

    while pq:
        cur_cost, now = heappop(pq)
        if now == e:
            return cur_cost

        temp[now] = 1
        
        for next_cost, next_node in edges[now]:
            if temp[next_node]:
                continue
            heappush(pq, (cur_cost + next_cost, next_node))


N, E = map(int, input().split())
edges = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    edges[a].append((c, b))
    edges[b].append((c, a))


u, v = map(int, input().split())


if not edges[N]:
    print(-1)
else:
    c1 = dijkstra(1, u, 0)
    c2 = dijkstra(u, v, c1)
    t1 = dijkstra(v, N, c2)
    
    c1 = dijkstra(1, v, 0)
    c2 = dijkstra(v, u, c1)
    t2 = dijkstra(u, N, c2)
    
    print(min(t1, t2))
