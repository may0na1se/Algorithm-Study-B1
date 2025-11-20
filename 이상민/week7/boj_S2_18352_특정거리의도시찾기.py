from collections import deque

N,M,K,X = map(int,input().split())
B = [[]for _ in range(N+1)]
V = [0]*(N+1)
for _ in range(M):
    s,e = map(int,input().split())
    B[s].append(e)

Q = deque([X])
V[X]=1

while Q:
    q = Q.popleft()
    if V[q]==K+2:break
    for b in B[q]:
        if V[b]: continue
        V[b]=V[q]+1
        Q.append(b)

f=1
for i in range(1,N+1):
    if V[i]==K+1:
        print(i)
        f=0

if f: print(-1)