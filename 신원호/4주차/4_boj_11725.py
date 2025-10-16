# boj 11725 트리의 부모 찾기

import sys
from collections import deque

N = int(input())
tree = [[] for _ in range(N + 1)]
# 양방향 그래프로 저장
for _ in range(N - 1):
    A, B = map(int, sys.stdin.readline().split())
    tree[B].append(A)
    tree[A].append(B)
parent = [0] * (N + 1)
route = deque([1])
parent[1] = 1
# 루트가 지정되어 있으므로 루트를 시작점으로 bfs
while route:
    now = route.popleft()
    for target in tree[now]:
        if not parent[target]:
            route.append(target)
            parent[target] = now

for i in range(2, N + 1):
    print(parent[i])