import sys
sys.stdin = open('1003/input.txt', 'r')


import heapq


N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((w,e))



INF = 10**7



start = X

dist = [0] + [INF] * N
dist[start] = 0
q = [(0,start)]
while q:
    cur_dist, cur_node = heapq.heappop(q)
    # if cur_node == 2 :
    #     break

    for next_d, next_node in graph[cur_node]:
        new_d = next_d + cur_dist
        if new_d < dist[next_node]:
            dist[next_node] = new_d
            heapq.heappush(q, (new_d, next_node))

# print(dist)      

dist_from_X_to_N = dist

dist_from_N_to_X = [0]
#X에서 마을로 돌아가는거리
# 
#  


for i in range(1, N+1):
    start = i

    dist = [0] + [INF] * N
    dist[start] = 0
    q = [(0,start)]
    while q:
        cur_dist, cur_node = heapq.heappop(q)
        if cur_node == X :
            break

        for next_d, next_node in graph[cur_node]:
            new_d = next_d + cur_dist
            if new_d < dist[next_node]:
                dist[next_node] = new_d
                heapq.heappush(q, (new_d, next_node))

    # print(dist[X])    
    dist_from_N_to_X.append(dist[X])

# print(dist_from_N_to_X, dist_from_X_to_N)

max_dist = 0
for a, b in zip(dist_from_N_to_X, dist_from_X_to_N):
    if a+b > max_dist:
        max_dist = a+b

print(max_dist)