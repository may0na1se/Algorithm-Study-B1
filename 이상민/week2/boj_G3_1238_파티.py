from heapq import heappop, heappush

def a(s):
    pq=[]
    heappush(pq,(0,s))
    while pq:
        w,n = heappop(pq)
        if w>=D[s][n]: continue
        D[s][n]=w
        for dw,nn in P[n]:
            if w+dw>=D[s][nn]:continue
            heappush(pq,(w+dw,nn))

N,M,X = map(int,input().split())
P = [[]for _ in range(N+1)]
D = [[float('inf')]*(N+1)for _ in range(N+1)]
for _ in range(M):
    s,e,w = map(int,input().split())
    P[s].append((w,e))
for s in range(1,N+1): a(s)
res = 0
for s in range(1,N+1):
    if s==X:continue
    r = D[s][X]+D[X][s]
    if r>res:res=r
print(res)