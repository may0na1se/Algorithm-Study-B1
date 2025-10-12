'''
문제: https://www.acmicpc.net/problem/11725
접근: 부모라는 말 보자마자 그냥 union-find로 풀어버림.
근데 그렇게 하면 root는 찾을 수 있는데, 바로 위 parent는 제대로 찾을 수가 없었음.
제미나이가 bfs로 풀면 된다더라...
1이 어차피 root니까 1부터 돌면 1과 연결된 노드들이 먼저 방문될 테고,
그러면 자연스럽게 아래 level에 있는 노드들의 parent가 알아서 갱신됨..

시간복잡도: O(N) bfs는 O(N)의 시간 복잡도를 가진다는구나!
'''

import sys
from collections import deque

N = int(input())

edges = [[] for _ in range(N + 1)]

parents = [i for i in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    edges[a].append(b)
    edges[b].append(a)

dq = deque([1])
visited[1] = 1

while dq:
    cur_node = dq.popleft()

    for next_node in edges[cur_node]:
        if visited[next_node]:
            continue
        parents[next_node] = cur_node

        visited[next_node] = 1
        dq.append(next_node)

for i in range(2, N+1):
    print(parents[i])