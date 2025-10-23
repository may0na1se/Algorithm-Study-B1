D = [(0,1),(1,0),(-1,0),(0,-1)]

def find(n):
    if n==P[n]:return n
    P[n] = find(P[n])
    return P[n]

def union(n,m):
    rn,rm = find(n),find(m)
    if rn==rm:return 1
    if S[rn]>S[rm]:rn,rm=rm,rn
    P[rn]=rm
    S[rm]+=S[rn]
    S[rn]=0
    return 0

N,M = map(int,input().split())
B = [[*map(int,input().split())]for _ in range(N)]
P = [*range(N*M)]
S = [1]*(N*M)

for r in range(N):
    for c in range(M):
        for d in D:
            dr,dc = r+d[0],c+d[1]
            if dr<0 or dr>=N or dc<0 or dc>=M: continue
            if B[dr][dc]==B[r][c]: union(r*M+c,dr*M+dc)

res=che=0

while True:
    V = []
    for r in range(N):
        for c in range(M):
            if B[r][c]==0:continue
            for d in D:
                dr,dc = r+d[0],c+d[1]
                if dr < 0 or dr >= N or dc < 0 or dc >= M: continue
                if find(M*dr+dc)==find(0):
                    V.append((r,c))
                    break

    P = [*range(N * M)]
    S = [1] * (N * M)

    if V:
        res+=1
        che=len(V)
        for r,c in V:
            B[r][c]=0
        for r in range(N):
            for c in range(M):
                for d in D:
                    dr, dc = r + d[0], c + d[1]
                    if dr < 0 or dr >= N or dc < 0 or dc >= M: continue
                    if B[dr][dc] == B[r][c]: union(r * M + c, dr * M + dc)
    else: break

print(res)
print(che)