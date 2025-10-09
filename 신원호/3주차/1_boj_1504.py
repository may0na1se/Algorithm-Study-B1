import sys
import heapq

def dijkstra(start, goal):
    q = [(0, start)]
    visited = [0] * (N + 1)
    distance = [float('inf')] * (N + 1)
    while q:
        dist, now = heapq.heappop(q)
        if now == goal:
            return dist
        distance[now] = dist
        if not visited[now]:
            visited[now] = 1
            for target in edge[now]:
                if not visited[target[1]]:
                    heapq.heappush(q, (dist + target[0], target[1]))
    return False

# 개선 버전
# def dijkstra(start, goal):
#     q = [(0, start)]
#     distance = [float('inf')] * (N + 1)
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         if dist > distance[now]:
#             continue
#         if now == goal:
#             return dist
#         for cost, nxt in edge[now]:
#             new_dist = dist + cost
#             if new_dist < distance[nxt]:
#                 distance[nxt] = new_dist
#                 heapq.heappush(q, (new_dist, nxt))
#     return False


N, E = map(int, input().split())
node = list(range(N + 1))
edge = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    edge[a].append((c, b))
    edge[b].append((c, a))
v1, v2 = map(int, input().split())
while True:
    # 1 -> v1, v2
    option1_1 = dijkstra(1, v1)
    option1_2 = dijkstra(1, v2)
    if option1_1 is False and option1_2 is False:
        print(-1)
        break
    # v1 -> v2
    mid = dijkstra(v1, v2)
    if mid is False:
        print(-1)
        break
    # v1, v2 -> N
    option2_1 = dijkstra(v1, N)
    option2_2 = dijkstra(v2, N)
    if option2_1 is False and option2_2 is False:
        print(-1)
        break
    result = mid + min(option1_1 + option2_2, option1_2 + option2_1)
    print(result)
    break