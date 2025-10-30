def a(n):
    r=0
    for p in P:
        r+=(p-1)//n
    return r

N,M,L = map(int,input().split())
if N: B = [0]+sorted([*map(int,input().split())])+[L]
else: B = [0,L]
P = [B[i]-B[i-1] for i in range(1,N+2)]


if N+M+1==L: print(1)

else:
    s,e=0,L
    while s<=e:
        m=(s+e)//2
        if m==0: m=1
        if a(m)>M: s=m+1
        else: e=m-1

    print(s)
    