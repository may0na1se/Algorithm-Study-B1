# boj 1967 트리의 지름
# 트리의 지름을 구하는 공식? 메커니즘을 알아야 한다.
# 무작위 정점에서 가장 먼 정점 A
# A에서 가장 먼 정점 B
# A - B가 트리의 지름

import sys
def dfs(n):
    route = [(n, 0)]
    visited = [0] * (N + 1)
    visited[n] = 1
    result = [0, 0]
    while route:
        now, distance = route[-1]
        count = 0
        if tree[now]:
            for target in tree[now]:
                node, edge = target[0], target[1]
                if not visited[node]:
                    route.append((node, distance + edge))
                    visited[node] = 1
                    count += 1
        if count == 0:
            if result[1] < distance:
                result = [now, distance]
            route.pop()
    return result

N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    parent, child, edge = map(int, sys.stdin.readline().split())
    tree[parent].append((child, edge))
    tree[child].append((parent, edge))

print(dfs(dfs(1)[0])[1])