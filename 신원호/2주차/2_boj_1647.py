import sys
import heapq

# MST 문제
# 간선의 개수가 충분히 많을 수 있으므로 Prim 알고리즘 사용
# MST를 만든 후에 임의의 간선을 제거하면 반드시 두개의 트리로 분할 가능하다.
# 따라서 MST를 완성한 후 그 중 가장 긴 간선을 제거하면 정답
N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    edges[a].append((c, b))
    edges[b].append((c, a))
q = []
result = 0
count = 0
visited = [False] * (N + 1)
now = 1
visited[1] = True
for target in edges[1]:
    heapq.heappush(q, (target[0], target[1]))
longest = 0
while count < N - 1:
    cost, node = heapq.heappop(q)
    if visited[node]:
        continue
    visited[node] = True
    result += cost
    longest = max(longest, cost)
    count += 1
    for nxt_cost, nxt in edges[node]:
        if not visited[nxt]:
            heapq.heappush(q, (nxt_cost, nxt))
print(result - longest)