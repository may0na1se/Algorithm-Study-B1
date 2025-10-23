N = int(input())
T = [[*map(int,input().split())] for _ in range(N)]
D = [[T[0][0]]]+[[0]*(i+1) for i in range(1,N)]
for i in range(1,N):
    D[i][0] = T[i][0] + D[i-1][0]
    for j in range(1,i):
        D[i][j] = max(T[i][j]+D[i-1][j],T[i][j]+D[i-1][j-1])
    D[i][-1] = T[i][-1]+D[i-1][-1]

print(max(D[-1]))