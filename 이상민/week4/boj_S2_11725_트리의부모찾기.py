from collections import deque

N,*P = [*map(int,open(0).read().split())]
V = [[]for _ in range(N+1)]
R = [0]*(N+1)

for r,c in zip(P[::2],P[1::2]):
    V[r].append(c)
    V[c].append(r)

Q = deque()
Q.append(1)

while Q:
    q = Q.popleft()
    for t in V[q]:
        if R[t]:continue
        R[t]=q
        Q.append(t)

print(*R[2:],sep='\n')