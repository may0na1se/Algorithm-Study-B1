from heapq import heappush,heappop

N,M = map(int,input().split())
P = [[] for _ in range(N+1)]
for _ in range(M):
    r,c,w = map(int,input().split())
    P[r].append((w,c))
    P[c].append((w,r))
res = road = 0
pq = []
heappush(pq,(0,1))
v = set()
while pq:
    w,n = heappop(pq)
    if n in v: continue
    res += w
    if w>road:road=w
    v.add(n)
    for nw,nn in P[n]:
        if nn in v: continue
        heappush(pq,(nw,nn))

print(res-road)