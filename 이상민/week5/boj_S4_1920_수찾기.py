def a(s,e,n):
    while s<=e:
        m=(s+e)//2
        b=B[m]
        if b==n: return 1
        elif b<n: s=m+1
        else: e=m-1
    return 0

N = int(input())
B = sorted(map(int,input().split()))
M = int(input())
P = [*map(int,input().split())]

for p in P:
    print(a(0,N-1,p))