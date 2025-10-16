def a(r):
    m=1
    mn=mx=P[0]
    for i in range(1,N):
        n = P[i]
        if n<mn and mx-n>r or n>mx and n-mn>r:
            m+=1
            mn=mx=n
        else:
            mn,mx = min(mn,n),max(mx,n)
        if m>M: return 0
    return 1

N,M = map(int,input().split())
P = [*map(int,input().split())]

e = max(P)-min(P)
s = 0

while s<=e:
    rr = (s+e)//2
    if a(rr):
        e = rr-1
    else: s = rr+1

print(s)