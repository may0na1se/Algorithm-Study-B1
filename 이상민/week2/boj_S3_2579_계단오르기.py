N = int(input())
P = [int(input()) for _ in range(N)]
if N == 1: print(P[0])
else:
    F0 = [0]*N
    F1 = [0]*N
    F0[0],F0[1],F1[1] = P[0],P[1],P[0]+P[1]
    for i in range(2,N):
        F0[i] = max(F0[i-2],F1[i-2])+P[i]
        F1[i] = F0[i-1]+P[i]
    print(max(F0[-1],F1[-1]))