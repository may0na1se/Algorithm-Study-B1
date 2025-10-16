'''
문제: https://www.acmicpc.net/problem/1647
접근: 양방향 그래프
1. 집이 연결된 것을 알아야 함 > union find
2. 개 중에서 비용이 가장 작은 경로를 찾아야 함 > kruskal or prim
3. 그리고 연결된 집들을 두개로 나눠야 함

시간복잡도: 몰?라
'''

import sys

def find_parents(x):
    if parents[x] == x:
        return x
    parents[x] = find_parents(parents[x])
    return parents[x]

def union_find(x, y):
    px, py = find_parents(x), find_parents(y)

    if px == py:
        return False
    
    # rank 써야할 수도 있음
    if px > py:
        px, py = py, px
    parents[py] = px
    return True

def kruskal():
    global costs
    global max_cost
    # 일단 1번부터 다 이어질 때까지 돌자
    for route in routes:
        cost, a, b = route
        if a > b:
            a, b = b, a
        if not union_find(a, b):
            continue

        # 어차피 경로를 한바퀴 순회하는 거 아니니까 result에 다 더해줄 필요 없을 듯?
        costs += cost
        if cost > max_cost:
            max_cost = cost



N, M = map(int, input().split())

routes = [0] * M

for i in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    routes[i] = (C, A, B)

routes.sort()

parents = [i for i in range(N+1)]
costs = 0
max_cost = 0

kruskal()

# 가장 비용이 큰 경로 하나를 자르기
print(costs - max_cost)
