from collections import deque

def a(s):
    Q = deque([s])
    V = [-1]*(N+1)
    V[s] = 0
    e = r = 0
    while Q:
        q = Q.popleft()
        for n,w in P[q]:
            if V[n]>=0: continue
            V[n]=V[q]+w
            Q.append(n)
    for i in range(1,N+1):
        if len(P[i])==1 and V[i]>r:
            r,e=V[i],i
    return r,e

N = int(input())
if N==1:print(0)
else:
    P = [[] for _ in range(N+1)]
    for i in range(N-1):
        r,c,w = map(int,input().split())
        P[r].append((c,w))
        P[c].append((r,w))
    
    for i in range(N+1):
        if len(P[i])==1:
            s=i
            break
    
    _,e = a(s)
    print(a(e)[0])