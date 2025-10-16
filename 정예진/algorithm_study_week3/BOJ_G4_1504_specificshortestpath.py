# 접근법 : 다익스트라를 시작 노드, 정점1, 정점 2에서 각각 돌린다
# 어차피 우리한테 필요한건 '어떤 경로를 거쳤느냐' 가 아니라 
# '얼마나 걸렸느냐', '거리가 얼마나 되느냐' 이기 때문에
# 시작 노드와 정점 1, 정점 2에서 각각 다익스트라 돌려서 가장 최단 거리로 N까지 도달하는 길을 찾는다
# 후보는 1 -> v1 -> v2 -> N  or  1 -> v2 -> v1 -> N 2개 뿐임
# 걸린 시간 : 20분?

import sys
from heapq import heappop, heappush

N, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

v1, v2 = map(int, sys.stdin.readline().split())
INF = float("INF")

def dijkstra(start):
    dist = [INF] * (N+1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, now = heappop(pq)

        if d > dist[now]:
            continue

        for dt, next in graph[now]:
            if dist[next] > d + dt:
                dist[next] = d+dt
                heappush(pq, (dist[next], next))
    return dist


dist1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

path1 = dist1[v1] + dist_v1[v2] + dist_v2[N]
path2 = dist1[v2] + dist_v2[v1] + dist_v1[N]

answer = min(path1,path2)
if answer == INF:
    print(-1)
else:
    print(answer)


