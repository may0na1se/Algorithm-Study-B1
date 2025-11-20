import sys
N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    p,c,w = map(int, sys.stdin.readline().split())
    graph[p].append((w,c))
    graph[c].append((w,p))

# 지금까지 생각한거 -> 트리가 이진트리인가? 
# 그렇다면 1번의 자식노드까지 오는 경로 나눠서 구하고 각 자식노드까지 오는데 가장 가중치의 합이 큰 것을 각각 골라 두개의 가중치 더하기
# 이진트리가 아니라면? 1번에서 리프까지 가는 모든 경로의 가중치 구하기 -> 제일 큰거 2개 더하기 (DFS)
# 이렇게 했을 때 문제 : 루트트리를 지나야만 하는 경로가 출력됨 -> 이건 안됨

# DFS 로 풀되 다른 접근 방식이 필요
# 풀이 시간 : 진짜 4시간...
# 임의의 한 노드로부터 가장 거리가 먼 한 노드를 찾고, 그 노드로부터 또 거리가 가장 먼 노드를 찾으면
# 트리의 지름이 된다

def dfs(start):
    visited = [0] * (N + 1)
    stack = [(0,start)]
    max_dist = 0
    farthest_node = start
    while stack:
        dist, node = stack.pop()
        if visited[node]:
            continue
        visited[node] = 1
        if dist > max_dist:
            max_dist = dist
            farthest_node = node
        for w, next_node in graph[node]:
            stack.append((dist+w, next_node))

    return farthest_node, max_dist


# 1단계: 임의의 노드에서 가장 먼 노드 찾기 - 임의노드 = 루트노드
A, _ = dfs(1)
# 2단계: 그 노드에서 가장 먼 노드까지 거리 찾기
_, diameter = dfs(A)
print(diameter)