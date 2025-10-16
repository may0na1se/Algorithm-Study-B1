N = int(input())
P = [*map(int,input().split())]

D = [0]*N
D[0] = P[0]

for i in range(1,N):
    D[i] = max(P[i],P[i]+D[i-1])

print(max(D))