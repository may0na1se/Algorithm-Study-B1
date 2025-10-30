N = int(input())
P = sorted(map(int,input().split()))
s,e=0,N-1
R=P[s]+P[e]
a,b=P[s],P[e]
while s<e:
    r=P[s]+P[e]
    if abs(R)>abs(r):
        R=r
        a,b=P[s],P[e]
    if r>0:
        e-=1
    else:s+=1
print(a,b)