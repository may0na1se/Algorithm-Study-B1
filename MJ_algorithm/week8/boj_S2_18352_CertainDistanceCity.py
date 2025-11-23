import sys
from collections import deque

sys.stdin = open('input.txt', 'r', encoding='utf-8-sig')
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

city = [[] for _ in range(N + 1)]  #도시번호, 길번호가 1부터

for _ in range(M):
    s, e = map(int, input().split())
    city[s].append(e)

dist = [-1] * (N+1)
dist[X] = 0

q = deque([X])
while q:
    cur_city = q.popleft()
    
    for next_city in city[cur_city]:
        if dist[next_city] == -1 :
            dist[next_city] = dist[cur_city] + 1
            q.append(next_city)
    
exists = False
for i in range(N+1):
    if dist[i] == K:
        print(i)
        exists = True

if exists == False:
    print(-1)