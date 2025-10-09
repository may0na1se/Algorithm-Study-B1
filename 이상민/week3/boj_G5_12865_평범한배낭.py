N,K = map(int,input().split())
W = [0]*N
V = [0]*N
for i in range(N):
    w,v = map(int,input().split())
    W[i],V[i] = w,v
B = [0]*(K+1)
for i in range(N):
    for j in range(K,W[i],-1):
        if B[j-W[i]] and B[j]<(V[i]+B[j-W[i]]):
            B[j] = V[i]+B[j-W[i]]
    if W[i]<=K and B[W[i]]<V[i]:
        B[W[i]] = V[i]

print(max(B))