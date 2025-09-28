import sys
import heapq


N, M, X = map(int, input().split())
# 뒤집은 그래프
go_party = [[] for _ in range(N + 1)]
# 원본 그래프
back_home = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, time = map(int, sys.stdin.readline().split())
    go_party[end].append((start, time))
    back_home[start].append((end, time))
# 왕복 거리의 합을 기록
result = [0] * (N + 1)

# dijkstra
q1 = [(0, X)]
visited = [False] * (N + 1)
while q1:
    distance, now = heapq.heappop(q1)
    if visited[now]:
        continue
    # 각 노드에 최초 방문 한 시점에서 현재 이동거리가 항상 최소
    visited[now] = True
    result[now] = distance
    for target in back_home[now]:
        if visited[target[0]]:
            continue
        heapq.heappush(q1, (distance + target[1], target[0]))
q2 = [(0, X)]
visited = [False] * (N + 1)
while q2:
    distance, now = heapq.heappop(q2)
    if visited[now]:
        continue
    visited[now] = True
    result[now] += distance
    for target in go_party[now]:
        if visited[target[0]]:
            continue
        heapq.heappush(q2, (distance + target[1], target[0]))
print(max(result))
