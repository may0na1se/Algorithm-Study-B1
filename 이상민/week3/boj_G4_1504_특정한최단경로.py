from heapq import heappop, heappush

def a(s,e):
    pq = []
    heappush(pq,(0,s))
    W = [float('inf')]*(N+1)
    while pq:
        w,n = heappop(pq)
        if w>=W[n]: continue
        W[n]=w
        for dw,nn in P[n]:
            if w+dw>=W[nn]:continue
            heappush(pq,(w+dw,nn))
    return W[1],W[e],W[N]

N,E = map(int,input().split())
P = [[]for _ in range(N+1)]
for _ in range(E):
    r,c,w = map(int,input().split())
    P[r].append((w,c))
    P[c].append((w,r))
s,e = map(int,input().split())
r1,m,c1,c2,_,r2 = *a(s,e),*a(e,s)
res = min(r1+r2,c1+c2)+m
print(-1 if res == float('inf') else res)