import sys
# input = sys.stdin.readline

sys.stdin = open('1003/input.txt', 'r')

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

edges = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

#heapq 써도 됨
edges.sort()

total_cost = 0
last_edge_cost = 0 

for edge in edges:  #길 하나씩 확인하면서 합치고 마지막 길=가장 먼 길 만 끊기
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        total_cost += cost
        last_edge_cost = cost 

print(total_cost - last_edge_cost)