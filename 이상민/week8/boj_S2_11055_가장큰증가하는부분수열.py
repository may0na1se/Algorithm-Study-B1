N = int(input())
B = [*map(int,input().split())]
S = [0]*N
S[0] = B[0]

for i in range(1,N):
    f = 1
    for j in range(i):
        if B[j]<B[i] and S[j]+B[i]>S[i]:
            S[i] = S[j]+B[i]
            f = 0
    if f: S[i]=B[i]

print(max(S))