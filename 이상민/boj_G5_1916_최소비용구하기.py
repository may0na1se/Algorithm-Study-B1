from heapq import heappop, heappush

def a():
    pq = []
    heappush(pq,(0,s))
    while pq:
        w,n = heappop(pq)
        if w>=D[n]: continue
        D[n]=w
        for dw,nn in P[n]:
            if w+dw>=D[nn]: continue
            heappush(pq,(w+dw,nn))

N = int(input())
M = int(input())
P = [[]for _ in range(N+1)]
D = [float('inf')]*(N+1)
for _ in range(M):
    s,e,w = map(int,input().split())
    P[s].append((w,e))
s,e = map(int,input().split())
a()
print(D[e])