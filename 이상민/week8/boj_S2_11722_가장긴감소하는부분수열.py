N = int(input())
A = [*map(int,input().split())]
B = [0]*N
B[0] = 1

for i in range(1,N):
    r=0
    for j in range(i):
        if A[i]<A[j] and r<B[j]:r=B[j]
    B[i]=r+1

print(max(B))