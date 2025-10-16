def a(n,r,p1,p2,p3,p4):
    if n==N:
        global Xr
        global Nr
        if r>Xr:Xr=r
        if r<Nr:Nr=r
        return
    if p1: a(n+1,r+B[n],p1-1,p2,p3,p4)
    if p2: a(n+1,r-B[n],p1,p2-1,p3,p4)
    if p3: a(n+1,r*B[n],p1,p2,p3-1,p4)
    if p4: a(n+1,int(r/B[n]),p1,p2,p3,p4-1)

N = int(input())
B = [*map(int,input().split())]
P = [*map(int,input().split())]
Xr = -int(21e8)
Nr = int(21e8)
a(1,B[0],*P)
print(Xr)
print(Nr)

