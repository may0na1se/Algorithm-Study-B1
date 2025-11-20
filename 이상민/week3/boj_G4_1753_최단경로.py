from heapq import heappop,heappush

N,E = map(int,input().split())
D = [float('inf')]*(N+1)
P = [[]for _ in range(N+1)]
s = int(input())

for _ in range(E):
    r,c,w = map(int,input().split())
    P[r].append((w,c))

pq = []
heappush(pq,(0,s))
while pq:
    w,n = heappop(pq)
    if w>=D[n]:continue
    D[n]=w
    for dw,nn in P[n]:
        if w+dw>=D[nn]: continue
        heappush(pq,(w+dw,nn))

for d in D[1:]: print(d if d!=float('inf') else 'INF')