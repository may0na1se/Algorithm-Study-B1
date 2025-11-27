N = int(input())
B = [*map(int,input().split())]
P = [*range(N)]
L = [1]*N

for i in range(1,N):
    for j in range(i):
        if L[j]<L[i] or B[j]>=B[i]: continue
        L[i] = L[j]+1
        P[i] = j

l = max(L)
s = L.index(l)
print(l)
R = [B[s]]
while P[s] != s:
    s = P[s]
    R.append(B[s])
print(*R[::-1])